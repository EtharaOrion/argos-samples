# TRUTH.md - feldroy__air-246

## Defect

The milestone bundles 1 announced issue(s):
1. (#55): Add function signatures to Air  SVG Tags

The reference change touches 7 file(s) in python. 6 target test(s) observe the result and 89 preserve test(s) must keep passing.

## Load-bearing work

The reference change lands in 2 file(s):

- `src/air/tags/models/svg.py`
- `mkdocs.yml`

What each file must end up doing is declared in `rubrics.json`, which is what the deterministic channel reads. This section names the files so a reader knows the shape of the work, not the text to type.

## Verification

Run the target test(s) recorded in `tests/config.json` (6) and confirm the preserve set (89) still passes.

## Root cause

Every tag class in the SVG model module is a bare subclass of the case‑preserving tag base: a name, a one‑line docstring, and nothing else. All attribute handling therefore falls through to the generic base constructor, which accepts an arbitrary keyword mapping and hands it straight to the attribute renderer.

Two consequences follow, and both are observable:

1. **Nothing removes `None`.** The base renderer only distinguishes booleans (bare attribute / omitted) from ordinary values; a keyword whose value is `None` is an ordinary value and is emitted as a literal attribute with the string form of `None` in it. A caller that builds an element from optional data — the normal case, e.g. `cy=maybe_missing` — gets junk markup. There is no layer between the caller and the renderer that could drop it, because the class contributes no code at all.

2. **There is no declared attribute surface.** Because the only entry point is `**kwargs`, the set of attributes each element supports is invisible to type checkers, to editors, and to the docs generator, and the rendered attribute order is whatever order the caller happened to type. Once elements *do* declare their attributes, the order becomes canonical (declaration order, with unrecognised extras appended), which is what markup‑level assertions for things like an animation element with timing attributes, an image element with experimental attributes, or a nested structure are written against.

So the failures are predictable without reading the fix: any test that passes an explicit `None`, or that pins the exact rendered attribute string for an element whose attributes it lists out of "natural" order, cannot pass while the classes are empty pass‑throughs.

A third, latent trap in this area: several SVG attributes are Python keywords or builtins (`from`, `in`, `class`, `type`, `id`, `filter`), and many are camelCase (`attributeName`, `repeatCount`, `calcMode`, `keyTimes`, `viewBox`, `preserveAspectRatio`, `gradientUnits`). The base performs underscore→hyphen mangling on keyword names, so how you spell a parameter directly determines the attribute that appears in the output.

## Solution shape

Give every SVG element class an explicit constructor whose parameters are its real attributes, and interpose a single shared filtering step between those parameters and the base tag.

Required properties of the end state:

- A module‑level helper takes the constructor's local variable mapping and returns only the attribute entries: it must exclude the instance, the variadic children collection, the pass‑through keyword mapping, and any name beginning with an underscore, and it must drop entries whose value *is* `None`. Values that are falsy but not `None` (`0`, `""`, `False`) must survive.
- Each element's constructor accepts variadic children first, then keyword‑only attributes each defaulting to `None`, then an open keyword mapping for anything not enumerated, and delegates to the base as roughly:

  ```
  constructor(self, *children, attr1=None, ..., class_=None, id=None, style=None, **extra):
      base_init(self, *children, **filter_locals(locals()), **extra)
  ```

  and it must call the filter before introducing any other local variable, otherwise that variable leaks into the attributes.
- Parameter spelling is the contract with the renderer: camelCase SVG attributes are spelled camelCase (snake_case would be mangled into hyphenated names and silently produce wrong markup); attributes that clash with Python syntax carry a trailing underscore and rely on the base's underscore stripping; hyphenated presentation attributes may be reached via underscore names or left to the open keyword mapping.
- The classes keep the case‑preserving base so element names such as the motion‑animation element, the filter primitives and the gradient elements still render with their original casing.
- Docstrings move to an `Args:`‑style block documenting children, each attribute, the DOM class/id/style trio, and the extras mapping, since these are what the API reference renders.
- The coverage must be the whole module, not the handful of elements the tests name — a document assembled from many element types is part of the observable behaviour.
- Documentation navigation must accommodate the now much larger reference: the single SVG API entry becomes a group (an overview plus alphabetically partitioned pages), with a real source page behind each nav entry.

## Ordered plan

1. **Read the failing expectations first.** They pin exact rendered strings: which attribute names appear, in what order, and what happens to a `None`. Everything downstream is calibrated against this, so do not start editing classes before you know whether attribute order is asserted.
2. **Read the base tag's attribute rendering.** You need to know precisely: does it strip a trailing underscore from every name or only from the class attribute; does it convert underscores to hyphens; how does it treat `True`/`False`; is the attribute dict insertion‑ordered. This decides whether the per‑class constructors need any name mapping of their own or whether correct parameter spelling suffices. Getting this wrong is invisible until markup is compared.
3. **Look at how the HTML element module already solves the same problem.** Mirroring its shape keeps the docs generator, the type stubs and the existing suite happy, and tells you what the filtering helper is expected to exclude.
4. **Write the filtering helper.** It is the single point where the `None`‑suppression property lives; implement it before touching classes so every class inherits the behaviour instead of each re‑deriving it.
5. **Convert two or three elements by hand and run the narrow tests** — one with plain attributes, one with keyword‑clashing or camelCase attributes, one that exercises pass‑through extras. Passing here proves the helper's exclusion list and the parameter‑spelling rules; failing here is much cheaper to diagnose than after a hundred conversions.
6. **Convert the remaining elements mechanically**, filling in the documented attribute set per element and leaving genuinely open‑ended or vendor attributes to the extras mapping. Only now is a bulk edit safe.
7. **Run the whole suite**, watching specifically for regressions in the previously passing tests, which are the ones most likely to be broken by attribute reordering or by an accidentally emitted extra attribute.
8. **Split and wire up the API reference pages last**, once the shape of the module is final: create the overview page and the alphabetical ranges, point each nav entry at a page that actually exists, and build the docs to confirm nothing dangles.

## Pitfalls

- **Filtering on truthiness instead of on `None`.** Dropping falsy values silently deletes `x=0`, `opacity=0`, `offset=""` and any explicitly false boolean. The test that checks omission only passes `None`, so this bug survives it.
- **Fixing only the elements the failing tests name.** The structural test composes many element types; and the general contract ("optional attributes disappear") must hold for every SVG element, including the filter primitives, gradients and text elements that no named test touches.
- **Snake‑casing camelCase SVG attributes.** A parameter named with underscores is mangled by the base into a hyphenated attribute, which browsers ignore. The animation and filter elements are full of these; the resulting markup looks plausible and is wrong.
- **Forgetting the keyword/builtin collisions.** The animation elements need the `from` attribute and the filter primitives need `in`; both must be reachable and must render unsuffixed. Verify against the base's stripping rule rather than assuming the class attribute is the only special case.
- **Creating locals before harvesting them.** Any convenience variable, loop index, or early normalisation computed inside the constructor before the filtering call becomes a bogus rendered attribute. Harvest first, then compute.
- **Letting the children tuple or the extras mapping into the attribute set,** or double‑passing the extras (once through the harvested locals and again as an unpacked mapping) — the latter raises a duplicate keyword error at call time on any element that receives an unrecognised attribute.
- **Adjusting a test's expected markup to whatever the new signature emits.** If attribute order changed because a parameter list was written in an arbitrary order, fix the declaration order to the canonical one rather than rewriting the expectation.
- **Dropping the case‑preserving base while refactoring**, which quietly lowercases the element names of the motion‑animation, gradient and filter‑primitive tags.
- **Adding nav entries without the corresponding documentation sources**, which breaks the docs build even though the test suite is green.

## Provenance

```yaml
uuid: 276ad6ba-10da-5f87-82ea-c2abc44dfdea
instance_id: feldroy__air-246
fix_patch_sha256: 0353f2ec3d93bcf1be2be6eb3c23e9a3c600c155af037cf02368a121afff9391
language: python
targets_total: 6
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
