# TRUTH.md - GitoxideLabs__gitoxide-2191

## Defect

The milestone bundles 1 announced issue(s):
1. (#2190): `credential fill` subcommand incorrectly assumes required field(s)

The reference change touches 4 file(s) in rust. 4 target test(s) observe the result and 2764 preserve test(s) must keep passing.

## Load-bearing work

The reference change lands in 4 file(s):

- `gix-credentials/src/program/main.rs`
- `gitoxide-core/src/repository/credential.rs`
- `gix-credentials/src/protocol/context/mod.rs`
- `gix-credentials/src/protocol/mod.rs`

What each file must end up doing is declared in `rubrics.json`, which is what the deterministic channel reads. This section names the files so a reader knows the shape of the work, not the text to type.

## Verification

Run the target test(s) recorded in `tests/config.json` (4) and confirm the preserve set (2764) still passes.

## Root cause

Git's credential protocol lets a caller describe a resource *either* by a single `url=` line *or* by the discrete fields `protocol=`, `host=` (plus optional `path=`, `username=`). `git credential fill` accepts both forms; the two are equivalent inputs.

Three places in this codebase treat `url` as the only legal input form:

1. **The context destructuring step** (the in-place routine that expands a context's url into its components and applies the "drop the path for http(s) unless `useHttpPath`" rule) begins by unwrapping the `url` field, and bails with the "url is missing" protocol error if it is empty. It never considers that the components it is about to *produce* may already be present.

2. **The credential-helper `main` entry point** validates incoming stdin context before dispatching a `Get`/fill action, and rejects any context whose `url` field is absent. So a well-formed request consisting of `protocol` + `host` is refused before the helper closure is ever called. The same function's "helper returned nothing" branch re-reads the raw stdin bytes, re-parses them, and `expect()`s a url in order to build the "no credentials found" error — an unwrap that is only safe *because* of the very gate being removed.

3. **The `credential fill` subcommand in the CLI** takes the parsed context and `expect()`s the url field, on the stated assumption that the framework guaranteed it. Once the gate above stops guaranteeing it, this is a panic on valid input; even today it is the reason the component form cannot work end to end.

Consequently: feeding `protocol=https` and `host=example.com` (no `url`) to the helper machinery yields a "url missing" error instead of a lookup, and reaching the CLI path with such a context would abort the process. The user-visible error messages also mis-state the protocol's requirement, claiming the url field is mandatory.

## Solution shape

The property to establish: **anywhere the code needs a URL for a credential context, it must accept a URL that was supplied directly *or* one reconstructed from the discrete fields, and only fail when neither is available.**

The context type already owns a routine that renders its components back into a url string (scheme, optional user, host — which may carry a port — and path); reuse it rather than hand-rolling assembly.

- Destructuring: if the url field is empty, fill it from the components first, then proceed with the existing parse-and-split logic unchanged. If no url can be produced, keep failing with the existing missing-url protocol error. After this, the parse of a synthesized string is what enforces well-formedness — a scheme with no host must not silently succeed.

  ```
  destructure(&mut self):
      if self.url absent:
          self.url = assemble_from_components() or return MissingUrl
      parsed = parse(self.url)          # may itself reject e.g. scheme-only input
      ...existing splitting / http-path rules...
  ```

- Helper `main`'s pre-dispatch validation: reject only when the url is absent **and** the pair (protocol, host) is not both present. Both branches of the disjunction must be genuinely accepted.

- Same function's "no credentials" branch: it must produce the url from the request it actually processed. Since the context is consumed by the helper invocation, retain a copy (or the url derived from it) beforehand, and resolve it as `direct url, else assembled from components` — a value guaranteed to exist by the validation just performed. Do not go back to the raw input bytes and unwrap.

- CLI fill: resolve the url the same way (direct, else assembled), and on absence surface the ordinary missing-url protocol error through the command's error type instead of panicking.

- Both error texts (the helper-program variant and the protocol variant) should state the real requirement: a url, or else protocol together with host.

## Ordered plan

1. **Read the context type first.** Find the existing component→url renderer and pin down exactly when it yields nothing (it keys off the scheme) and what it emits when the host is absent. Everything downstream depends on this: it determines whether the "only one of protocol/host given" case is rejected by your explicit check or by url parsing. Confirm the port lives inside the host field so you don't double-append it.

2. **Fix the destructuring routine.** It is the shared primitive that both the helper program and the higher-level cascade funnel through; fixing it first means the callers only need their guards relaxed, not their logic rewritten. Verify with the two destructure-level tests: a context with scheme, host and path must come out carrying a fully-formed url (note the path stays in the url even though the http-path rule may clear the separate `path` field), and a context missing either scheme or host with no url must still error.

3. **Relax the helper program's input validation** to the either/or condition. Run the helper-program test for the component-only input; it will now get past validation and into the helper closure.

4. **Repair the "helper produced nothing" error path in the same function**, which the previous step just broke: the context has been moved into the helper call and the old code reconstructed the url by re-parsing stdin and unwrapping. Keep a copy before the call and derive the url from it with the same direct-or-assembled rule. This step must come after step 3 because it is step 3 that makes the old unwrap reachable and wrong.

5. **Fix the CLI fill path** to resolve the url the same way and to return, not panic, when it cannot. This is a separate crate and won't be caught by the credentials-crate unit tests; check it deliberately.

6. **Update the two error messages**, then run the whole suite — the destructuring change touches the shared cascade used by ordinary clone/fetch credential lookups, so regressions there would show up as changed url or path fields in existing expectations.

## Pitfalls

- **Fixing only the gate in the helper program.** Validation would pass, then the destructuring step immediately reports the url as missing again. Conversely, fixing only the destructuring step leaves the entry-point gate rejecting the request before it is reached. Both are needed; the CLI is a third, independent site that no credentials-crate test exercises.

- **Accepting a bare protocol.** The component renderer produces a string from a scheme alone, so writing the guard as "url present, or components can be rendered" wrongly admits `protocol=https` with no host and produces something like a scheme with an empty authority. The named test for the one-of-two case exists precisely to catch this; require *both* protocol and host when the url is absent.

- **Reconstructing the "no credentials found" url from the raw stdin buffer.** It looks like a faithful preservation of existing behaviour, but that path unwraps the url field of a freshly parsed request — which is now legitimately empty. It compiles, passes the happy-path tests, and panics on exactly the input this change is meant to support. Keeping the context around costs a clone; take it.

- **Synthesizing unconditionally, or after parsing.** If a url was supplied, it wins; overwriting it from components (which at that point may be stale or empty) changes behaviour for every existing caller. Assemble only when the field is empty, and do it before the parse/split, not after — doing it after means the http-path stripping has already run and the reconstructed url will be missing the path.

- **Weakening the test instead of the code**, e.g. having the destructure routine tolerate a context with no url at all by returning early without populating anything. Downstream code then receives a context whose url field is empty and fails later, further from the cause.

- **Assuming the one-of-two failure surfaces as the missing-url error.** Depending on the renderer, it may surface as a url-parse error instead; assert that an error occurs rather than pinning a specific variant, and don't add a redundant guard that changes which error existing callers observe.

## Provenance

```yaml
uuid: 24d2a5dc-2e40-5735-8fe2-342c4fd8e311
instance_id: GitoxideLabs__gitoxide-2191
fix_patch_sha256: 7217c0ff87aa7e89b3f38d5f95aa17204483049ae59558220c1ef39f7dbf5840
language: rust
targets_total: 4
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
