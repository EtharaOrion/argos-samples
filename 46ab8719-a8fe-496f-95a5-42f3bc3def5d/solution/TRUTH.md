# TRUTH.md - DTStack__molecule-641

## Defect

The milestone bundles 1 announced issue(s):
1. (#627): How to get current theme?

The reference change touches 3 file(s) in typescript. 2 target test(s) observe the result and 695 preserve test(s) must keep passing.

## Load-bearing work

The reference change lands in 3 file(s):

- `src/common/utils.ts`
- `src/services/theme/colorThemeService.ts`
- `src/model/colorTheme.ts`

What each file must end up doing is declared in `rubrics.json`, which is what the deterministic channel reads. This section names the files so a reader knows the shape of the work, not the text to type.

## Verification

Run the target test(s) recorded in `tests/config.json` (2) and confirm the preserve set (695) still passes.

## Root cause

Nothing in the codebase can answer the question "is the theme currently in effect a light one or a dark one?".

`IColorTheme` carries a `type` field typed by the existing `ColorScheme` enum, but two things make that field unusable on its own as an answer:

1. It is optional and frequently absent. Themes imported from VS Code extension packages, and the built-in themes shipped in the workbench, are largely a `colors` map plus `tokenColors`; many have no `type` at all. A consumer reading `colorTheme.type` gets `undefined` and has no fallback.
2. It has three members, not two. High-contrast is a distinct scheme value, so a consumer that compares against the two obvious members mishandles it silently.

`IColorThemeService` exposes getters for the theme list, the current theme, and colors, but no derived "which side of the spectrum is this" accessor, so every widget that needs to pick an icon set, a shadow, or a syntax fallback has to reimplement the inference — and there is no primitive to reimplement it with. `src/common/utils.ts` has id/search helpers only; there is no function anywhere that takes a CSS color string and classifies its perceived brightness. So both the low-level capability and the service-level accessor are missing, and both named tests fail at import/`undefined is not a function` time rather than on a wrong value.

## Solution shape

Two independent pieces plus a wiring step.

**A brightness classifier in the shared utils module.** A pure exported function taking one CSS color string and returning one of two literal strings — the ordinary English words for the two ends of the brightness scale, i.e. the lowercased forms of the existing `ColorScheme` members. It must accept, at minimum:

- `#rrggbb`
- three-digit shorthand (`#abc`), which has to be expanded by doubling each digit before parsing — parsing it directly gives a wildly wrong channel split
- `rgb(r, g, b)` and `rgba(r, g, b, a)`, with arbitrary whitespace after the commas and a fractional alpha

and it must not throw on the ones it does not recognise. Classification must be perceptual, not a channel average: weight the squared channels roughly 0.30/0.59/0.11 (red/green/blue), take the square root, and compare against the midpoint of the 0–255 range. A plain mean of R,G,B misclassifies saturated blues and yellows and will not match the expectations in the utility test.

```
classify(color):
    if color starts with the rgb prefix:
        pull the three integer channels out with a regex tolerant of an optional 4th, fractional, component
    else:
        normalise to six hex digits (expand shorthand, ignore anything past the 6th)
        split into three bytes via shifts/masks
    weighted = sqrt(0.299*r^2 + 0.587*g^2 + 0.114*b^2)
    return weighted > 255/2 ? brighter-mode : darker-mode
```

**A two-member enum for theme mode** in the color-theme model, whose string values are exactly the two strings the classifier returns. This is what the service's return type is expressed in, so the classifier's output can be treated as one of its members.

**A public accessor on the color theme service**, declared on the service interface (not just the class) so it is reachable through the injected/`molecule.colorTheme` handle. Its contract, evaluated against *the theme in effect at call time*, not a value captured earlier:

1. If the theme declares a scheme, map it: the dark scheme *and* the high-contrast scheme both yield the darker mode; the light scheme yields the brighter one.
2. Otherwise, look for a representative surface fill in the theme's `colors` map, trying in order the editor's surface-fill key, then the active tab's, then molecule's welcome-view surface key, and run the first one found through the classifier.
3. If neither path produces anything (no scheme, empty or absent `colors`), return the darker mode as the default — molecule's baseline theme is dark.

Every step must tolerate `colors` being `undefined`.

## Ordered plan

1. **Add the mode enum to the color-theme model first.** Both the service signature and (via a cast) the classifier's consumers refer to it; introducing it up front means step 3 compiles without a temporary `string` return type that you would then have to widen. Confirm its two string values line up with what the classifier will emit — if they diverge the cast in step 3 is a lie that TypeScript will not catch.
2. **Write the classifier in the shared utils module, and exercise it in isolation before touching the service.** It has the only non-trivial logic (three input syntaxes, one formula), and the utility test targets it directly. Getting it green here means any later failure in the service test is a dispatch/ordering problem, not an arithmetic one. Check the shorthand-hex case and an `rgba` with a decimal alpha explicitly; those are the two branches easiest to get subtly wrong and hardest to notice from a single `#ffffff`/`#000000` smoke test.
3. **Add the method to the service class and mirror it on the service interface.** Declaring only on the class compiles fine but consumers typed as the interface (including the exported molecule API surface) cannot call it — the service test may pass while real usage does not. Implement the three-tier precedence in the order above.
4. **Verify precedence with a theme that contradicts itself** — a declared light scheme whose editor surface is near-black. The declared scheme must win; if the color inference wins you have the tiers inverted, which no single-tier test detects.
5. **Verify the default path** by asking for the mode on a theme with neither a scheme nor any of the three surface keys, and re-verify after `setTheme` to a different theme that the answer changes — that catches an implementation that read the theme once in the constructor.
6. **Run the full suite last.** The enum addition touches an exported model module; make sure no existing switch over color-theme types or snapshot of the model's exports has become non-exhaustive.

## Pitfalls

- **Stopping at the declared scheme.** A version that returns based on `type` alone satisfies "themes have a type" intuition but returns the wrong answer for the majority of real themes, which ship colors only. The service test specifically drives the color-inference path.
- **Forgetting high contrast.** Treating only the explicitly-dark scheme as dark leaves high-contrast falling through to the color heuristic or to the default. It happens to reach the same answer via the default here, which is exactly why an incorrect mapping goes unnoticed until someone adds a light high-contrast variant.
- **Averaging the channels, or comparing hex strings.** `(r+g+b)/3 > 127` is a one-liner that passes for pure black and pure white and fails for `#0000ff` / `#ffff00`. Use the luminance weighting.
- **Parsing shorthand hex as if it were full-length.** `parseInt('#abc'.slice(1), 16)` yields a three-digit number; the red channel shift then produces 0 and everything shorthand is classified as very dark. Expand to six digits first.
- **Choking on an 8-digit hex with alpha.** Take only the first six digits after the `#` rather than letting the alpha bytes overflow into the red-channel shift.
- **A regex that only matches `rgb(`.** The alpha form must be accepted, and the fourth component can be fractional; a pattern requiring `\d+` for it will silently fall into the hex branch and produce `NaN` channels.
- **Assuming the colors map exists.** Themes with only token colors, and the empty default theme, have no color map; unguarded indexing throws inside a getter that callers will invoke during render.
- **Caching the answer.** Computing the mode when the service is constructed, or memoising it, breaks theme switching — the accessor must re-read the current theme each call.
- **Class-only declaration.** Adding the method without extending the service interface leaves it invisible to anything holding the injected/exported handle, which is the whole point of the request.

## Provenance

```yaml
uuid: 46ab8719-a8fe-496f-95a5-42f3bc3def5d
instance_id: DTStack__molecule-641
fix_patch_sha256: ae8c2922c968e831a86212d409ebef620b5602957f77be5d470c2fe435b0115a
language: typescript
targets_total: 2
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
