
WARNING: apt does not have a stable CLI interface. Use with caution in scripts.

Get:1 http://deb.debian.org/debian trixie InRelease [140 kB]
Get:2 http://deb.debian.org/debian trixie-updates InRelease [47.3 kB]
Get:3 http://deb.debian.org/debian-security trixie-security InRelease [43.4 kB]
Get:4 http://deb.debian.org/debian trixie/main arm64 Packages [9607 kB]
Get:5 http://deb.debian.org/debian trixie-updates/main arm64 Packages [4424 B]
Get:6 http://deb.debian.org/debian-security trixie-security/main arm64 Packages [252 kB]
Fetched 10.1 MB in 1s (12.8 MB/s)
Reading package lists...
Building dependency tree...
Reading state information...
All packages are up to date.

WARNING: apt does not have a stable CLI interface. Use with caution in scripts.

Reading package lists...
Building dependency tree...
Reading state information...
patch is already the newest version (2.8-2).
patch set to manually installed.
Summary:
  Upgrading: 0, Installing: 0, Removing: 0, Not Upgrading: 0
============================= test session starts ==============================
platform linux -- Python 3.11.16, pytest-9.1.1, pluggy-1.6.0 -- /usr/local/bin/python3.11
cachedir: .pytest_cache
rootdir: /home/air
configfile: pyproject.toml
plugins: cov-7.1.0, anyio-4.15.1
collecting ... collected 96 items

tests/test_applications.py::test_air_app_factory PASSED                  [  1%]
tests/test_applications.py::test_air_plus_fastapi PASSED                 [  2%]
tests/test_applications.py::test_page_decorator PASSED                   [  3%]
tests/test_applications.py::test_air_404_response PASSED                 [  4%]
tests/test_applications.py::test_default_500_exception_handler PASSED    [  5%]
tests/test_background.py::test_background_task_in_view PASSED            [  6%]
tests/test_background.py::test_add_background_task PASSED                [  7%]
tests/test_forms.py::test_form_sync_check FAILED                         [  8%]
tests/test_forms.py::test_form_validation_dependency_injection PASSED    [  9%]
tests/test_forms.py::test_form_validation_in_view PASSED                 [ 10%]
tests/test_forms.py::test_form_render PASSED                             [ 11%]
tests/test_forms.py::test_form_render_with_values PASSED                 [ 12%]
tests/test_forms.py::test_form_render_in_view PASSED                     [ 13%]
tests/test_forms.py::test_form_render_with_errors PASSED                 [ 14%]
tests/test_forms.py::test_html_input_field_types PASSED                  [ 15%]
tests/test_forms.py::test_air_field PASSED                               [ 16%]
tests/test_forms.py::test_airform_notimplementederror PASSED             [ 17%]
tests/test_layouts.py::test_pico_layout PASSED                           [ 18%]
tests/test_layouts.py::test_mvpcss_layout PASSED                         [ 19%]
tests/test_layouts.py::test_mvpcss_layout_header PASSED                  [ 20%]
tests/test_requests.py::test_is_htmx PASSED                              [ 21%]
tests/test_responses.py::test_TagResponse_obj PASSED                     [ 22%]
tests/test_responses.py::test_TagResponse_type PASSED                    [ 23%]
tests/test_responses.py::test_TagResponse_html PASSED                    [ 25%]
tests/test_responses.py::test_strings_and_tag_children PASSED            [ 26%]
tests/test_responses.py::test_custom_name_in_response PASSED             [ 27%]
tests/test_responses.py::test_TagResponse_with_layout_strings PASSED     [ 28%]
tests/test_responses.py::test_TagResponse_with_layout_names PASSED       [ 29%]
tests/test_responses.py::test_AirResponse PASSED                         [ 30%]
tests/test_responses.py::test_SSEResponse PASSED                         [ 31%]
tests/test_responses.py::test_SSEResponse_multiline_tag_content PASSED   [ 32%]
tests/test_responses.py::test_SSEResponse_string_content PASSED          [ 33%]
tests/test_svg.py::test_atag_no_attrs_no_children PASSED                 [ 34%]
tests/test_svg.py::test_atag_with_all_attributes FAILED                  [ 35%]
tests/test_svg.py::test_cased_tag_no_children PASSED                     [ 36%]
tests/test_svg.py::test_cased_tags_with_children PASSED                  [ 37%]
tests/test_svg.py::test_circle_with_attributes PASSED                    [ 38%]
tests/test_svg.py::test_rect_with_all_attributes FAILED                  [ 39%]
tests/test_svg.py::test_ellipse_coordinates PASSED                       [ 40%]
tests/test_svg.py::test_line_coordinates FAILED                          [ 41%]
tests/test_svg.py::test_path_with_data PASSED                            [ 42%]
tests/test_svg.py::test_svg_with_viewbox FAILED                          [ 43%]
tests/test_svg.py::test_group_with_children FAILED                       [ 44%]
tests/test_svg.py::test_text_with_positioning FAILED                     [ 45%]
tests/test_svg.py::test_tspan_in_text PASSED                             [ 46%]
tests/test_svg.py::test_linear_gradient_with_stops FAILED                [ 47%]
tests/test_svg.py::test_radial_gradient FAILED                           [ 48%]
tests/test_svg.py::test_filter_with_effects FAILED                       [ 50%]
tests/test_svg.py::test_fe_distant_light PASSED                          [ 51%]
tests/test_svg.py::test_fe_drop_shadow FAILED                            [ 52%]
tests/test_svg.py::test_animate_with_values FAILED                       [ 53%]
tests/test_svg.py::test_animate_motion_with_path FAILED                  [ 54%]
tests/test_svg.py::test_marker_definition FAILED                         [ 55%]
tests/test_svg.py::test_mask_with_content FAILED                         [ 56%]
tests/test_svg.py::test_complex_svg_structure FAILED                     [ 57%]
tests/test_svg.py::test_none_attributes_filtered PASSED                  [ 58%]
tests/test_svg.py::test_mixed_type_attributes FAILED                     [ 59%]
tests/test_svg.py::test_image_with_experimental_attributes FAILED        [ 60%]
tests/test_svg.py::test_script_with_experimental_attributes FAILED       [ 61%]
tests/test_svg.py::test_animate_with_extended_attributes FAILED          [ 62%]
tests/test_tags.py::test_atag_no_attrs_no_children PASSED                [ 63%]
tests/test_tags.py::test_atag_yes_attrs_no_children PASSED               [ 64%]
tests/test_tags.py::test_atag_yes_attrs_text_children PASSED             [ 65%]
tests/test_tags.py::test_divtag_yes_attrs_a_child PASSED                 [ 66%]
tests/test_tags.py::test_divtag_yes_attrs_multiple_a_children PASSED     [ 67%]
tests/test_tags.py::test_divtag_yes_attrs_nested_children PASSED         [ 68%]
tests/test_tags.py::test_name_types PASSED                               [ 69%]
tests/test_tags.py::test_subclassing PASSED                              [ 70%]
tests/test_tags.py::test_subclassing_nested PASSED                       [ 71%]
tests/test_tags.py::test_text_child_with_sibling_elements PASSED         [ 72%]
tests/test_tags.py::test_special_attributes PASSED                       [ 73%]
tests/test_tags.py::test_raw_html_basic PASSED                           [ 75%]
tests/test_tags.py::test_raw_html_with_script PASSED                     [ 76%]
tests/test_tags.py::test_raw_html_invalid_args PASSED                    [ 77%]
tests/test_tags.py::test_raw_html_ignores_kwargs PASSED                  [ 78%]
tests/test_tags.py::test_functions_as_tags PASSED                        [ 79%]
tests/test_tags.py::test_pico_card PASSED                                [ 80%]
tests/test_tags.py::test_tags_head_tag_injection PASSED                  [ 81%]
tests/test_tags.py::test_escape_html PASSED                              [ 82%]
tests/test_tags.py::test_script_tag PASSED                               [ 83%]
tests/test_tags.py::test_style_tag PASSED                                [ 84%]
tests/test_tags.py::test_tags_support_global_attributes PASSED           [ 85%]
tests/test_tags.py::test_special_characters PASSED                       [ 86%]
tests/test_tags.py::test_bool_attributes PASSED                          [ 87%]
tests/test_tags.py::test_self_closing_tags PASSED                        [ 88%]
tests/test_tags.py::test_children_tag PASSED                             [ 89%]
tests/test_tags.py::test_tag_generation PASSED                           [ 90%]
tests/test_tags.py::test_safestr PASSED                                  [ 91%]
tests/test_tags.py::test_other_children_types PASSED                     [ 92%]
tests/test_tags.py::test_tag_for_tag_subclass_wrapper PASSED             [ 93%]
tests/test_templates.py::test_JinjaRenderer PASSED                       [ 94%]
tests/test_templates.py::test_JinjaRenderer_no_context PASSED            [ 95%]
tests/test_templates.py::test_JinjaRenderer_with_Air PASSED              [ 96%]
tests/test_templates.py::test_JinjaRenderer_with_kwargs PASSED           [ 97%]
tests/test_templates.py::test_jinja_plus_airtags PASSED                  [ 98%]
tests/test_templates.py::test_jinja_plus_airtags_autorender PASSED       [100%]

=================================== FAILURES ===================================
_____________________________ test_form_sync_check _____________________________

    def test_form_sync_check():
        class CheeseModel(BaseModel):
            name: str
            age: int
    
        class CheeseForm(air.AirForm):
            model = CheeseModel
    
        cheese = CheeseForm()
        cheese.validate({"name": "Parmesan", "age": "Hello"})
        assert cheese.is_valid is False
>       assert cheese.errors == [
            {
                "type": "int_parsing",
                "loc": ("age",),
                "msg": "Input should be a valid integer, unable to parse string as an integer",
                "input": "Hello",
                "url": "https://errors.pydantic.dev/2.11/v/int_parsing",
            }
        ]
E       AssertionError: assert [{'type': 'in...'Hello', ...}] == [{'type': 'in...'Hello', ...}]
E         
E         At index 0 diff: {'type': 'int_parsing', 'loc': ('age',), 'msg': 'Input should be a valid integer, unable to parse string as an integer', 'input': 'Hello', 'url': 'https://errors.pydantic.dev/2.13/v/int_parsing'} != {'type': 'int_parsing', 'loc': ('age',), 'msg': 'Input should be a valid integer, unable to parse string as an integer', 'input': 'Hello', 'url': 'https://errors.pydantic.dev/2.11/v/int_parsing'}
E         
E         Full diff:
E           [
E               {
E                   'type': 'int_parsing',...
E         
E         ...Full output truncated (11 lines hidden), use '-vv' to show

tests/test_forms.py:22: AssertionError
________________________ test_atag_with_all_attributes _________________________

    def test_atag_with_all_attributes():
        link = air.svg.A(
            "Link text",
            href="https://example.com",
            target="_blank",
            download="file.pdf",
            hreflang="en-US",
            ping="https://tracker.example.com",
            referrerpolicy="no-referrer",
            rel="noopener",
            type="application/pdf",
        )
        expected = '<a href="https://example.com" target="_blank" download="file.pdf" hreflang="en-US" ping="https://tracker.example.com" referrerpolicy="no-referrer" rel="noopener" type="application/pdf">Link text</a>'
>       assert link.render() == expected
E       assert '<a href="htt...Link text</a>' == '<a href="htt...Link text</a>'
E         
E         - <a href="https://example.com" target="_blank" download="file.pdf" hreflang="en-US" ping="https://tracker.example.com" referrerpolicy="no-referrer" rel="noopener" type="application/pdf">Link text</a>
E         ?                               ----------------
E         + <a href="https://example.com" download="file.pdf" hreflang="en-US" ping="https://tracker.example.com" referrerpolicy="no-referrer" rel="noopener" target="_blank" type="application/pdf">Link text</a>
E         ?                                                                                                                                                  ++++++++++++++++

tests/test_svg.py:21: AssertionError
________________________ test_rect_with_all_attributes _________________________

    def test_rect_with_all_attributes():
        rect = air.svg.Rect(x=10, y=20, width=100, height=50, rx=5, ry=3, pathLength=300)
        expected = '<rect x="10" y="20" width="100" height="50" rx="5" ry="3" pathLength="300"></rect>'
>       assert rect.render() == expected
E       assert '<rect height...="20"></rect>' == '<rect x="10"..."300"></rect>'
E         
E         - <rect x="10" y="20" width="100" height="50" rx="5" ry="3" pathLength="300"></rect>
E         + <rect height="50" pathLength="300" rx="5" ry="3" width="100" x="10" y="20"></rect>

tests/test_svg.py:45: AssertionError
____________________________ test_line_coordinates _____________________________

    def test_line_coordinates():
        line = air.svg.Line(x1=0, y1=0, x2=100, y2=100, style="stroke: black;")
        expected = '<line x1="0" y1="0" x2="100" y2="100" style="stroke: black;"></line>'
>       assert line.render() == expected
E       assert '<line x1="0"...ack;"></line>' == '<line x1="0"...ack;"></line>'
E         
E         - <line x1="0" y1="0" x2="100" y2="100" style="stroke: black;"></line>
E         ?             -------
E         + <line x1="0" x2="100" y1="0" y2="100" style="stroke: black;"></line>
E         ?                       +++++++

tests/test_svg.py:57: AssertionError
____________________________ test_svg_with_viewbox _____________________________

    def test_svg_with_viewbox():
        svg = air.svg.Svg(width=200, height=200, viewBox="0 0 200 200", id="main-svg")
        expected = (
            '<svg width="200" height="200" viewBox="0 0 200 200" id="main-svg"></svg>'
        )
>       assert svg.render() == expected
E       assert '<svg height=...n-svg"></svg>' == '<svg width="...n-svg"></svg>'
E         
E         - <svg width="200" height="200" viewBox="0 0 200 200" id="main-svg"></svg>
E         ?     ------------
E         + <svg height="200" viewBox="0 0 200 200" width="200" id="main-svg"></svg>
E         ?                                        ++++++++++++

tests/test_svg.py:72: AssertionError
___________________________ test_group_with_children ___________________________

    def test_group_with_children():
        group = air.svg.G(
            air.svg.Circle(r=10),
            air.svg.Rect(width=20, height=20),
            class_="shape-group",
            id="group1",
        )
        expected = '<g class="shape-group" id="group1"><circle r="10"></circle><rect width="20" height="20"></rect></g>'
>       assert group.render() == expected
E       assert '<g class="sh..."></rect></g>' == '<g class="sh..."></rect></g>'
E         
E         - <g class="shape-group" id="group1"><circle r="10"></circle><rect width="20" height="20"></rect></g>
E         ?                                                                  -----------
E         + <g class="shape-group" id="group1"><circle r="10"></circle><rect height="20" width="20"></rect></g>
E         ?                                                                        +++++++++++

tests/test_svg.py:83: AssertionError
__________________________ test_text_with_positioning __________________________

    def test_text_with_positioning():
        text = air.svg.Text("Hello SVG", x=50, y=100, dx=5, dy=-10, textLength=80)
        expected = '<text x="50" y="100" dx="5" dy="-10" textLength="80">Hello SVG</text>'
>       assert text.render() == expected
E       assert '<text dx="5"...lo SVG</text>' == '<text x="50"...lo SVG</text>'
E         
E         - <text x="50" y="100" dx="5" dy="-10" textLength="80">Hello SVG</text>
E         ?      ---------------
E         + <text dx="5" dy="-10" textLength="80" x="50" y="100">Hello SVG</text>
E         ?                                      +++++++++++++++

tests/test_svg.py:90: AssertionError
_______________________ test_linear_gradient_with_stops ________________________

    def test_linear_gradient_with_stops():
        stop1 = air.svg.Stop(offset="0%", stop_color="red")
        stop2 = air.svg.Stop(offset="100%", stop_color="blue", stop_opacity=0.8)
        gradient = air.svg.LinearGradient(
            stop1, stop2, x1="0%", y1="0%", x2="100%", y2="0%", id="myGradient"
        )
        expected = '<linearGradient x1="0%" y1="0%" x2="100%" y2="0%" id="myGradient"><stop offset="0%" stop-color="red"></stop><stop offset="100%" stop-color="blue" stop-opacity="0.8"></stop></linearGradient>'
>       assert gradient.render() == expected
E       assert '<linearGradi...nearGradient>' == '<linearGradi...nearGradient>'
E         
E         - <linearGradient x1="0%" y1="0%" x2="100%" y2="0%" id="myGradient"><stop offset="0%" stop-color="red"></stop><stop offset="100%" stop-color="blue" stop-opacity="0.8"></stop></linearGradient>
E         ?                        --------
E         + <linearGradient x1="0%" x2="100%" y1="0%" y2="0%" id="myGradient"><stop offset="0%" stop-color="red"></stop><stop offset="100%" stop-color="blue" stop-opacity="0.8"></stop></linearGradient>
E         ?                                   ++++++++

tests/test_svg.py:108: AssertionError
_____________________________ test_radial_gradient _____________________________

    def test_radial_gradient():
        gradient = air.svg.RadialGradient(
            cx="50%",
            cy="50%",
            r="50%",
            fx="25%",
            fy="25%",
            gradientUnits="objectBoundingBox",
        )
        expected = '<radialGradient cx="50%" cy="50%" r="50%" fx="25%" fy="25%" gradientUnits="objectBoundingBox"></radialGradient>'
>       assert gradient.render() == expected
E       assert '<radialGradi...dialGradient>' == '<radialGradi...dialGradient>'
E         
E         - <radialGradient cx="50%" cy="50%" r="50%" fx="25%" fy="25%" gradientUnits="objectBoundingBox"></radialGradient>
E         ?                                   --------
E         + <radialGradient cx="50%" cy="50%" fx="25%" fy="25%" gradientUnits="objectBoundingBox" r="50%"></radialGradient>
E         ?                                                                                      ++++++++

tests/test_svg.py:121: AssertionError
___________________________ test_filter_with_effects ___________________________

    def test_filter_with_effects():
        blur = air.svg.FeGaussianBlur(in_="SourceGraphic", stdDeviation=2, result="blur")
        offset = air.svg.FeOffset(in_="blur", dx=3, dy=3, result="offset")
        filter_elem = air.svg.Filter(
            blur, offset, x="-20%", y="-20%", width="140%", height="140%", id="drop-shadow"
        )
        expected = '<filter x="-20%" y="-20%" width="140%" height="140%" id="drop-shadow"><feGaussianBlur in-="SourceGraphic" stdDeviation="2" result="blur"></feGaussianBlur><feOffset in-="blur" dx="3" dy="3" result="offset"></feOffset></filter>'
>       assert filter_elem.render() == expected
E       assert '<filter heig...set></filter>' == '<filter x="-...set></filter>'
E         
E         - <filter x="-20%" y="-20%" width="140%" height="140%" id="drop-shadow"><feGaussianBlur in-="SourceGraphic" stdDeviation="2" result="blur"></feGaussianBlur><feOffset in-="blur" dx="3" dy="3" result="offset"></feOffset></filter>
E         + <filter height="140%" width="140%" x="-20%" y="-20%" id="drop-shadow"><feGaussianBlur result="blur" in="SourceGraphic" stdDeviation="2"></feGaussianBlur><feOffset result="offset" dx="3" dy="3" in="blur"></feOffset></filter>

tests/test_svg.py:132: AssertionError
_____________________________ test_fe_drop_shadow ______________________________

    def test_fe_drop_shadow():
        shadow = air.svg.FeDropShadow(
            dx=2, dy=2, stdDeviation=1, flood_color="black", flood_opacity=0.3
        )
        expected = '<feDropShadow dx="2" dy="2" stdDeviation="1" flood-color="black" flood-opacity="0.3"></feDropShadow>'
>       assert shadow.render() == expected
E       assert '<feDropShado...feDropShadow>' == '<feDropShado...feDropShadow>'
E         
E         - <feDropShadow dx="2" dy="2" stdDeviation="1" flood-color="black" flood-opacity="0.3"></feDropShadow>
E         ?                            -----------------
E         + <feDropShadow dx="2" dy="2" flood-color="black" flood-opacity="0.3" stdDeviation="1"></feDropShadow>
E         ?                                                                    +++++++++++++++++

tests/test_svg.py:146: AssertionError
___________________________ test_animate_with_values ___________________________

    def test_animate_with_values():
        animate = air.svg.Animate(
            attributeName="opacity", values="0;1;0", dur="2s", repeatCount="indefinite"
        )
        expected = '<animate attributeName="opacity" values="0;1;0" dur="2s" repeatCount="indefinite"></animate>'
>       assert animate.render() == expected
E       assert '<animate att...0"></animate>' == '<animate att...e"></animate>'
E         
E         - <animate attributeName="opacity" values="0;1;0" dur="2s" repeatCount="indefinite"></animate>
E         ?                                  ---------------
E         + <animate attributeName="opacity" dur="2s" repeatCount="indefinite" values="0;1;0"></animate>
E         ?                                                                   +++++++++++++++

tests/test_svg.py:155: AssertionError
________________________ test_animate_motion_with_path _________________________

    def test_animate_motion_with_path():
        motion = air.svg.AnimateMotion(path="M10,10 L90,90", dur="3s", rotate="auto")
        expected = (
            '<animateMotion path="M10,10 L90,90" rotate="auto" dur="3s"></animateMotion>'
        )
>       assert motion.render() == expected
E       assert '<animateMoti...nimateMotion>' == '<animateMoti...nimateMotion>'
E         
E         - <animateMotion path="M10,10 L90,90" rotate="auto" dur="3s"></animateMotion>
E         ?                                                 ---------
E         + <animateMotion dur="3s" path="M10,10 L90,90" rotate="auto"></animateMotion>
E         ?                +++++++++

tests/test_svg.py:163: AssertionError
____________________________ test_marker_definition ____________________________

    def test_marker_definition():
        marker = air.svg.Marker(
            air.svg.Path(d="M0,0 L10,5 L0,10 Z"),
            markerWidth=10,
            markerHeight=10,
            refX=0,
            refY=5,
            orient="auto",
            id="arrow",
        )
        expected = '<marker markerWidth="10" markerHeight="10" refX="0" refY="5" orient="auto" id="arrow"><path d="M0,0 L10,5 L0,10 Z"></path></marker>'
>       assert marker.render() == expected
E       assert '<marker mark...ath></marker>' == '<marker mark...ath></marker>'
E         
E         - <marker markerWidth="10" markerHeight="10" refX="0" refY="5" orient="auto" id="arrow"><path d="M0,0 L10,5 L0,10 Z"></path></marker>
E         ?        -----------------                     ^^    ---------
E         + <marker markerHeight="10" markerWidth="10" orient="auto" refX="0" refY="5" id="arrow"><path d="M0,0 L10,5 L0,10 Z"></path></marker>
E         ?                           ++ + ^^^^^^  +                ++++++++++++++++++

tests/test_svg.py:178: AssertionError
____________________________ test_mask_with_content ____________________________

    def test_mask_with_content():
        mask = air.svg.Mask(
            air.svg.Rect(width="100%", height="100%", style="fill: white;"),
            air.svg.Circle(cx=50, cy=50, r=30, style="fill: black;"),
            id="hole-mask",
        )
        expected = '<mask id="hole-mask"><rect width="100%" height="100%" style="fill: white;"></rect><circle cx="50" cy="50" r="30" style="fill: black;"></circle></mask>'
>       assert mask.render() == expected
E       assert '<mask id="ho...ircle></mask>' == '<mask id="ho...ircle></mask>'
E         
E         - <mask id="hole-mask"><rect width="100%" height="100%" style="fill: white;"></rect><circle cx="50" cy="50" r="30" style="fill: black;"></circle></mask>
E         ?                            -------------
E         + <mask id="hole-mask"><rect height="100%" width="100%" style="fill: white;"></rect><circle cx="50" cy="50" r="30" style="fill: black;"></circle></mask>
E         ?                                          +++++++++++++

tests/test_svg.py:188: AssertionError
__________________________ test_complex_svg_structure __________________________

    def test_complex_svg_structure():
        # Create a complete SVG with multiple elements
        defs = air.svg.Defs(
            air.svg.LinearGradient(
                air.svg.Stop(offset="0%", stop_color="red"),
                air.svg.Stop(offset="100%", stop_color="blue"),
                id="grad1",
            )
        )
    
        content = air.svg.G(
            air.svg.Circle(cx=50, cy=50, r=40, style="fill: url(#grad1);"),
            air.svg.Text("SVG", x=35, y=55, style="font-family: Arial;"),
            class_="main-content",
        )
    
        svg = air.svg.Svg(
            defs,
            content,
            width=100,
            height=100,
            viewBox="0 0 100 100",
            xmlns="http://www.w3.org/2000/svg",
        )
    
        expected = '<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 100 100"><defs><linearGradient id="grad1"><stop offset="0%" stop-color="red"></stop><stop offset="100%" stop-color="blue"></stop></linearGradient></defs><g class="main-content"><circle cx="50" cy="50" r="40" style="fill: url(#grad1);"></circle><text x="35" y="55" style="font-family: Arial;">SVG</text></g></svg>'
>       assert svg.render() == expected
E       assert '<svg height=...xt></g></svg>' == '<svg xmlns="...xt></g></svg>'
E         
E         - <svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 100 100"><defs><linearGradient id="grad1"><stop offset="0%" stop-color="red"></stop><stop offset="100%" stop-color="blue"></stop></linearGradient></defs><g class="main-content"><circle cx="50" cy="50" r="40" style="fill: url(#grad1);"></circle><text x="35" y="55" style="font-family: Arial;">SVG</text></g></svg>
E         ?                                        -----------------------------------------------
E         + <svg height="100" viewBox="0 0 100 100" width="100" xmlns="http://www.w3.org/2000/svg"><defs><...
E         
E         ...Full output truncated (2 lines hidden), use '-vv' to show

tests/test_svg.py:218: AssertionError
__________________________ test_mixed_type_attributes __________________________

    def test_mixed_type_attributes():
        # Test that both string and numeric values work
        rect = air.svg.Rect(x="10px", y=20, width="50%", height=30.5)
        expected = '<rect x="10px" y="20" width="50%" height="30.5"></rect>'
>       assert rect.render() == expected
E       assert '<rect height...="20"></rect>' == '<rect x="10p...30.5"></rect>'
E         
E         - <rect x="10px" y="20" width="50%" height="30.5"></rect>
E         + <rect height="30.5" width="50%" x="10px" y="20"></rect>

tests/test_svg.py:234: AssertionError
___________________ test_image_with_experimental_attributes ____________________

    def test_image_with_experimental_attributes():
        # Test fetchpriority experimental attribute
        image = air.svg.Image(
            x=10,
            y=20,
            width=100,
            height=80,
            href="image.jpg",
            fetchpriority="high",
            crossorigin="anonymous",
        )
        expected = '<image x="10" y="20" width="100" height="80" href="image.jpg" crossorigin="anonymous" fetchpriority="high"></image>'
>       assert image.render() == expected
E       assert '<image fetch..."20"></image>' == '<image x="10...igh"></image>'
E         
E         - <image x="10" y="20" width="100" height="80" href="image.jpg" crossorigin="anonymous" fetchpriority="high"></image>
E         + <image fetchpriority="high" crossorigin="anonymous" height="80" href="image.jpg" width="100" x="10" y="20"></image>

tests/test_svg.py:250: AssertionError
___________________ test_script_with_experimental_attributes ___________________

    def test_script_with_experimental_attributes():
        # Test fetchpriority experimental attribute
        script = air.svg.Script(
            type="application/javascript",
            href="script.js",
            fetchpriority="low",
            crossorigin="use-credentials",
        )
        expected = '<script type="application/javascript" href="script.js" crossorigin="use-credentials" fetchpriority="low"></script>'
>       assert script.render() == expected
E       assert '<script fetc...pt"></script>' == '<script type...ow"></script>'
E         
E         - <script type="application/javascript" href="script.js" crossorigin="use-credentials" fetchpriority="low"></script>
E         + <script fetchpriority="low" crossorigin="use-credentials" href="script.js" type="application/javascript"></script>

tests/test_svg.py:262: AssertionError
____________________ test_animate_with_extended_attributes _____________________

    def test_animate_with_extended_attributes():
        # Test the additional animation attributes
        animate = air.svg.Animate(
            attributeName="opacity",
            attributeType="CSS",
            from_="0",
            to="1",
            by="0.5",
            dur="2s",
            begin="1s",
            end="5s",
            repeatCount="3",
            repeatDur="10s",
            calcMode="linear",
        )
        expected = '<animate attributeName="opacity" attributeType="CSS" dur="2s" repeatCount="3" repeatDur="10s" from-="0" to="1" by="0.5" begin="1s" end="5s" calcMode="linear"></animate>'
>       assert animate.render() == expected
E       assert '<animate att...1"></animate>' == '<animate att...r"></animate>'
E         
E         - <animate attributeName="opacity" attributeType="CSS" dur="2s" repeatCount="3" repeatDur="10s" from-="0" to="1" by="0.5" begin="1s" end="5s" calcMode="linear"></animate>
E         + <animate attributeName="opacity" attributeType="CSS" begin="1s" by="0.5" calcMode="linear" dur="2s" end="5s" from="0" repeatCount="3" repeatDur="10s" to="1"></animate>

tests/test_svg.py:281: AssertionError
==================================== PASSES ====================================
=========================== short test summary info ============================
PASSED tests/test_applications.py::test_air_app_factory
PASSED tests/test_applications.py::test_air_plus_fastapi
PASSED tests/test_applications.py::test_page_decorator
PASSED tests/test_applications.py::test_air_404_response
PASSED tests/test_applications.py::test_default_500_exception_handler
PASSED tests/test_background.py::test_background_task_in_view
PASSED tests/test_background.py::test_add_background_task
PASSED tests/test_forms.py::test_form_validation_dependency_injection
PASSED tests/test_forms.py::test_form_validation_in_view
PASSED tests/test_forms.py::test_form_render
PASSED tests/test_forms.py::test_form_render_with_values
PASSED tests/test_forms.py::test_form_render_in_view
PASSED tests/test_forms.py::test_form_render_with_errors
PASSED tests/test_forms.py::test_html_input_field_types
PASSED tests/test_forms.py::test_air_field
PASSED tests/test_forms.py::test_airform_notimplementederror
PASSED tests/test_layouts.py::test_pico_layout
PASSED tests/test_layouts.py::test_mvpcss_layout
PASSED tests/test_layouts.py::test_mvpcss_layout_header
PASSED tests/test_requests.py::test_is_htmx
PASSED tests/test_responses.py::test_TagResponse_obj
PASSED tests/test_responses.py::test_TagResponse_type
PASSED tests/test_responses.py::test_TagResponse_html
PASSED tests/test_responses.py::test_strings_and_tag_children
PASSED tests/test_responses.py::test_custom_name_in_response
PASSED tests/test_responses.py::test_TagResponse_with_layout_strings
PASSED tests/test_responses.py::test_TagResponse_with_layout_names
PASSED tests/test_responses.py::test_AirResponse
PASSED tests/test_responses.py::test_SSEResponse
PASSED tests/test_responses.py::test_SSEResponse_multiline_tag_content
PASSED tests/test_responses.py::test_SSEResponse_string_content
PASSED tests/test_svg.py::test_atag_no_attrs_no_children
PASSED tests/test_svg.py::test_cased_tag_no_children
PASSED tests/test_svg.py::test_cased_tags_with_children
PASSED tests/test_svg.py::test_circle_with_attributes
PASSED tests/test_svg.py::test_ellipse_coordinates
PASSED tests/test_svg.py::test_path_with_data
PASSED tests/test_svg.py::test_tspan_in_text
PASSED tests/test_svg.py::test_fe_distant_light
PASSED tests/test_svg.py::test_none_attributes_filtered
PASSED tests/test_tags.py::test_atag_no_attrs_no_children
PASSED tests/test_tags.py::test_atag_yes_attrs_no_children
PASSED tests/test_tags.py::test_atag_yes_attrs_text_children
PASSED tests/test_tags.py::test_divtag_yes_attrs_a_child
PASSED tests/test_tags.py::test_divtag_yes_attrs_multiple_a_children
PASSED tests/test_tags.py::test_divtag_yes_attrs_nested_children
PASSED tests/test_tags.py::test_name_types
PASSED tests/test_tags.py::test_subclassing
PASSED tests/test_tags.py::test_subclassing_nested
PASSED tests/test_tags.py::test_text_child_with_sibling_elements
PASSED tests/test_tags.py::test_special_attributes
PASSED tests/test_tags.py::test_raw_html_basic
PASSED tests/test_tags.py::test_raw_html_with_script
PASSED tests/test_tags.py::test_raw_html_invalid_args
PASSED tests/test_tags.py::test_raw_html_ignores_kwargs
PASSED tests/test_tags.py::test_functions_as_tags
PASSED tests/test_tags.py::test_pico_card
PASSED tests/test_tags.py::test_tags_head_tag_injection
PASSED tests/test_tags.py::test_escape_html
PASSED tests/test_tags.py::test_script_tag
PASSED tests/test_tags.py::test_style_tag
PASSED tests/test_tags.py::test_tags_support_global_attributes
PASSED tests/test_tags.py::test_special_characters
PASSED tests/test_tags.py::test_bool_attributes
PASSED tests/test_tags.py::test_self_closing_tags
PASSED tests/test_tags.py::test_children_tag
PASSED tests/test_tags.py::test_tag_generation
PASSED tests/test_tags.py::test_safestr
PASSED tests/test_tags.py::test_other_children_types
PASSED tests/test_tags.py::test_tag_for_tag_subclass_wrapper
PASSED tests/test_templates.py::test_JinjaRenderer
PASSED tests/test_templates.py::test_JinjaRenderer_no_context
PASSED tests/test_templates.py::test_JinjaRenderer_with_Air
PASSED tests/test_templates.py::test_JinjaRenderer_with_kwargs
PASSED tests/test_templates.py::test_jinja_plus_airtags
PASSED tests/test_templates.py::test_jinja_plus_airtags_autorender
FAILED tests/test_forms.py::test_form_sync_check - AssertionError: assert [{'...
FAILED tests/test_svg.py::test_atag_with_all_attributes - assert '<a href="ht...
FAILED tests/test_svg.py::test_rect_with_all_attributes - assert '<rect heigh...
FAILED tests/test_svg.py::test_line_coordinates - assert '<line x1="0"...ack;...
FAILED tests/test_svg.py::test_svg_with_viewbox - assert '<svg height=...n-sv...
FAILED tests/test_svg.py::test_group_with_children - assert '<g class="sh..."...
FAILED tests/test_svg.py::test_text_with_positioning - assert '<text dx="5".....
FAILED tests/test_svg.py::test_linear_gradient_with_stops - assert '<linearGr...
FAILED tests/test_svg.py::test_radial_gradient - assert '<radialGradi...dialG...
FAILED tests/test_svg.py::test_filter_with_effects - assert '<filter heig...s...
FAILED tests/test_svg.py::test_fe_drop_shadow - assert '<feDropShado...feDrop...
FAILED tests/test_svg.py::test_animate_with_values - assert '<animate att...0...
FAILED tests/test_svg.py::test_animate_motion_with_path - assert '<animateMot...
FAILED tests/test_svg.py::test_marker_definition - assert '<marker mark...ath...
FAILED tests/test_svg.py::test_mask_with_content - assert '<mask id="ho...irc...
FAILED tests/test_svg.py::test_complex_svg_structure - assert '<svg height=.....
FAILED tests/test_svg.py::test_mixed_type_attributes - assert '<rect height.....
FAILED tests/test_svg.py::test_image_with_experimental_attributes - assert '<...
FAILED tests/test_svg.py::test_script_with_experimental_attributes - assert '...
FAILED tests/test_svg.py::test_animate_with_extended_attributes - assert '<an...
======================== 20 failed, 76 passed in 0.51s =========================
