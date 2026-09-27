# TRUTH.md - secdev__scapy-3461

## Defect

The milestone bundles 1 announced issue(s):
1. (#3460): RTCP packet support

The reference change touches 1 file(s) in python. 3 target test(s) observe the result and 4242 preserve test(s) must keep passing.

## Load-bearing work

The reference change lands in 1 file(s):

- `scapy/contrib/rtcp.py`

What each file must end up doing is declared in `rubrics.json`, which is what the deterministic channel reads. This section names the files so a reader knows the shape of the work, not the text to type.

## Verification

Run the target test(s) recorded in `tests/config.json` (3) and confirm the preserve set (4242) still passes.

## Root cause

The failing tests dissect three byte strings taken from real RFC 3550 control traffic (a receiver report, a sender report, and a source-description report) and then assert on named attributes of the resulting layer. Today the codebase has no dissector for the control companion of RTP at all: the contrib loader has nothing to import, so the test file dies at load time; even if it got that far, the bytes would be interpreted as an opaque payload and every attribute lookup would fail. This is a missing-feature defect, not a mis-dissection one, so "predicting the failure" means predicting the shape the dissector must have — and that is where the real traps are, because a naive scapy layer for this protocol dissects the first test vector correctly and the other two wrongly.

The protocol structure that drives all of it (RFC 3550 §6):

* A 4-byte common header: 2-bit version (always 2 here), 1-bit padding flag, 5-bit item count, 8-bit packet type (200 sender report, 201 receiver report, 202 source description, 203 goodbye, 204 application-defined), 16-bit length. The length is **not** a byte count: it is the size of the whole compound unit in 32-bit words, minus one. Anything past that length in the buffer belongs to the next report stacked in the same datagram.
* Sender and receiver reports carry the reporter's synchronisation source, then (sender reports only) a 20-byte sender-info block of 64-bit NTP timestamp, RTP timestamp, packet count and octet count, then *count* fixed 24-byte reception report blocks: reportee source, 8-bit loss fraction, **24-bit** cumulative loss, extended highest sequence number, interarrival jitter, timestamp of last sender report, delay since it.
* Source description carries *count* chunks, each a source identifier followed by a variable-length list of type/length/text items, terminated by a zero type octet and then null-padded up to the next 4-byte boundary.

The mechanical trap: in scapy, a `Packet` subclass used inside a list field consumes everything after its own fields as its payload unless it is told that it has none. A dissector written without that hook will parse the first reception report block and hang the remaining blocks off it as raw payload, so a report list that should have three entries has one; likewise the sender-info block will swallow all following report blocks. So a version of this layer can make the receiver-report vector look right while the sender-report vector is silently mangled.

## Solution shape

Add a loadable contrib module for this protocol whose top-level layer, when handed the raw bytes of a control packet, yields:

* header semantics: version, padding flag, item count and numeric packet type readable as fields, with the type rendered through an enumeration covering at least 200–204;
* for types 200/201: the reporter's source id, and a list of reception report blocks whose length equals the header's item count, each block exposing all seven RFC fields with the cumulative-loss field occupying exactly three octets;
* for type 200 only, additionally the sender-info block between the source id and the report list;
* for type 202: a list of chunks equal in number to the item count, each chunk exposing its source id and its decoded items with their type (enumerated: end, canonical name, name, email, phone, location, tool, note, private) and text.

Properties any correct implementation must have, however it is spelled:

```
for every nested structure used inside a list field:
    when dissecting, it claims only its own bytes and returns the
    remainder to the enclosing list, never as its own payload

report/chunk list length  <- derived at dissection time from the header count field
header count field        <- derived at build time from the length of the corresponding list
presence of each optional group <- predicate on the parsed packet-type value

on serialisation, before returning the bytes:
    overwrite the 16-bit length slot with (total_octets_of_this_layer // 4) - 1
```

The last one cannot be expressed by a normal automatic-length field: scapy's length fields count bytes and generally only of a designated field or payload, whereas here the value covers the header plus all conditional groups and is expressed in words minus one. It has to be patched after the layer's own bytes exist.

For source description, chunk item parsing is not count-driven: the item list ends when the next type octet is zero, and the chunk then consumes the terminator plus enough nulls to land on a 4-byte boundary, so that the following chunk starts at the right offset.

The module must also carry the module-level metadata comments the contrib inventory expects (a human description and a load status), and must **not** register itself on any UDP port at import time; port association is left to the user via layer binding, and is documented in the module docstring.

## Ordered plan

1. **Read the three test vectors alongside RFC 3550 §6.** They tell you exactly which packet types and which attributes are observed, and whether the sender report vector contains more than one report block (it must, or the padding trap stays invisible). Everything after this depends on knowing the observed field set.
2. **Create the contrib module skeleton with the metadata comments and a docstring, containing only the enumeration tables and an empty top layer, and confirm it loads.** A contrib module that fails to import produces failures that look like dissection bugs; clearing that first makes every later failure meaningful. This also settles the "no automatic port binding" decision before anything else can accidentally depend on it.
3. **Define the fixed-size leaf structures first (report block, sender info), each with the hook that keeps its trailing bytes out of its own payload.** They are the pieces the container refers to, and defining the container first forces a rewrite. Sanity-check by dissecting a hand-cut 24-byte slice and confirming the seven fields and that the 24-bit loss field does not eat into the sequence number.
4. **Build the common header with the bit-packed first two octets plus the length, and add the receiver-report group (source id + count-driven block list).** Receiver report is the smallest complete case; if its block list has the right cardinality and the right values, the padding hook and the count-driven list are both proven. This is the point where a missing hook shows up as a one-element list.
5. **Add the sender-info group gated on type 200.** It reuses everything proved in step 4; the only new failure mode is the sender-info structure swallowing the following blocks, which step 4 has taught you to recognise.
6. **Add source description last.** It needs a different list-termination strategy (sentinel byte plus alignment) than the count-driven lists, so doing it after the count-driven path is working prevents conflating the two mechanisms. Verify chunk count matches the header count, not just that the first chunk parses.
7. **Only now implement the build side:** count fields computed from list lengths, and the post-serialisation rewrite of the length slot. It depends on the final field layout being settled; doing it earlier means redoing it. Validate by re-serialising each dissected test vector and comparing to the original bytes — this catches word-vs-byte and off-by-one errors in the length that dissection alone never exercises.
8. **Run the whole suite.** The only plausible cross-test damage is an import-time port binding or a name collision in the contrib inventory; both were fixed by construction in step 2, so this is confirmation rather than discovery.

## Pitfalls

* **Applying the "no payload of my own" hook to only one nested class.** Putting it on the report block but not on the sender-info structure makes the receiver-report test pass and quietly reduces the sender report's block list to zero or one entry. Every structure that appears inside a list or as an embedded sub-packet needs it.
* **Driving the report/chunk count off the header length field instead of the count field.** It appears to work on single-report test vectors and is wrong for compound datagrams (several reports concatenated, which is the normal case on the wire) and gives you nothing usable when building.
* **Using a stock automatic length field for the 16-bit length.** It will emit a byte count, or count only a payload, and the packets will still dissect fine from the fixture bytes — so the parse tests pass and every packet you *emit* is malformed. The value is words-minus-one over the header plus all conditional groups, and it can only be computed once those groups are serialised.
* **Letting the layer consume the whole remaining buffer.** Bytes beyond the declared length belong to the next report in the compound packet and must be handed on as payload; absorbing them makes stacked reports undissectable.
* **Source-description details:** treating the zero terminator as a real item and reading a length byte after it; forgetting the null padding to the 4-byte boundary, which desynchronises the second and later chunks; or assuming the item text is length-prefixed by anything other than the single octet after the type.
* **Field widths:** the cumulative-loss field is three octets, not four, and the NTP timestamp is a single 64-bit quantity in the RFC layout — widening or splitting either one shifts every subsequent field and produces plausible-looking but wrong numbers.
* **Registering a UDP port at import time** (or binding under RTP) to make the fixtures "just work". Control traffic has no fixed port; a hardcoded binding changes dissection for unrelated tests and datagrams. Leave the association to the caller and say so in the docstring.
* **Adjusting expectations to the implementation** — e.g. asserting a single report block, or asserting the length field equals the octet count — turns the test into a description of the bug. The expected values must come from the RFC reading of the captured bytes.
* **Omitting the contrib metadata comments.** The module then loads in isolation but fails the inventory/status checks that scan contrib modules, showing up as an unrelated regression among the other tests.

## Provenance

```yaml
uuid: 4056d683-bddd-57a4-8cf3-e807654c7c9c
instance_id: secdev__scapy-3461
fix_patch_sha256: 4675baacb99fb486db9e8e789bb5c297d252e24e9e35bb24da51feaf7ae13c4d
language: python
targets_total: 3
authored_by: generated
status: verified_reference
golden_score_measured: 1.0
golden_score_runs: 1
golden_score_verified_by: recorded_test_results
caveat: >
  Probes are literal substrings of the reference hunks, so the
  golden-patch probe gate passes by construction and is not
  evidence of probe quality for this bundle.
```
