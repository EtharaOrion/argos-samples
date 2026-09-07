
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
13 packages can be upgraded. Run 'apt list --upgradable' to see them.

WARNING: apt does not have a stable CLI interface. Use with caution in scripts.

Reading package lists...
Building dependency tree...
Reading state information...
patch is already the newest version (2.8-2).
patch set to manually installed.
Summary:
  Upgrading: 0, Installing: 0, Removing: 0, Not Upgrading: 13
============================= test session starts ==============================
platform linux -- Python 3.11.16, pytest-9.1.1, pluggy-1.6.0 -- /usr/local/bin/python3.11
cachedir: .pytest_cache
rootdir: /home/air
configfile: pyproject.toml
plugins: cov-7.1.0, anyio-4.15.0
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
tests/test_svg.py::test_rect_with_all_attributes PASSED                  [ 39%]
tests/test_svg.py::test_ellipse_coordinates PASSED                       [ 40%]
tests/test_svg.py::test_line_coordinates PASSED                          [ 41%]
tests/test_svg.py::test_path_with_data PASSED                            [ 42%]
tests/test_svg.py::test_svg_with_viewbox PASSED                          [ 43%]
tests/test_svg.py::test_group_with_children PASSED                       [ 44%]
tests/test_svg.py::test_text_with_positioning PASSED                     [ 45%]
tests/test_svg.py::test_tspan_in_text PASSED                             [ 46%]
tests/test_svg.py::test_linear_gradient_with_stops PASSED                [ 47%]
tests/test_svg.py::test_radial_gradient PASSED                           [ 48%]
tests/test_svg.py::test_filter_with_effects FAILED                       [ 50%]
tests/test_svg.py::test_fe_distant_light PASSED                          [ 51%]
tests/test_svg.py::test_fe_drop_shadow PASSED                            [ 52%]
tests/test_svg.py::test_animate_with_values PASSED                       [ 53%]
tests/test_svg.py::test_animate_motion_with_path PASSED                  [ 54%]
tests/test_svg.py::test_marker_definition FAILED                         [ 55%]
tests/test_svg.py::test_mask_with_content PASSED                         [ 56%]
tests/test_svg.py::test_complex_svg_structure FAILED                     [ 57%]
tests/test_svg.py::test_none_attributes_filtered PASSED                  [ 58%]
tests/test_svg.py::test_mixed_type_attributes PASSED                     [ 59%]
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
E         + <a href="https://example.com" target="_blank" download="file.pdf" rel="noopener" hreflang="en-US" type="application/pdf" referrerpolicy="no-referrer" ping="https://tracker.example.com">Link text</a>

tests/test_svg.py:21: AssertionError
___________________________ test_filter_with_effects ___________________________

    def test_filter_with_effects():
        blur = air.svg.FeGaussianBlur(in_="SourceGraphic", stdDeviation=2, result="blur")
        offset = air.svg.FeOffset(in_="blur", dx=3, dy=3, result="offset")
        filter_elem = air.svg.Filter(
            blur, offset, x="-20%", y="-20%", width="140%", height="140%", id="drop-shadow"
        )
        expected = '<filter x="-20%" y="-20%" width="140%" height="140%" id="drop-shadow"><feGaussianBlur in-="SourceGraphic" stdDeviation="2" result="blur"></feGaussianBlur><feOffset in-="blur" dx="3" dy="3" result="offset"></feOffset></filter>'
>       assert filter_elem.render() == expected
E       assert '<filter x="-...set></filter>' == '<filter x="-...set></filter>'
E         
E         - <filter x="-20%" y="-20%" width="140%" height="140%" id="drop-shadow"><feGaussianBlur in-="SourceGraphic" stdDeviation="2" result="blur"></feGaussianBlur><feOffset in-="blur" dx="3" dy="3" result="offset"></feOffset></filter>
E         ?                                                                                         -                                                                             -
E         + <filter x="-20%" y="-20%" width="140%" height="140%" id="drop-shadow"><feGaussianBlur in="SourceGraphic" stdDeviation="2" result="blur"></feGaussianBlur><feOffset in="blur" dx="3" dy="3" result="offset"></feOffset></filter>

tests/test_svg.py:132: AssertionError
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
E         ?                                            ------------------
E         + <marker markerWidth="10" markerHeight="10" orient="auto" refX="0" refY="5" id="arrow"><path d="M0,0 L10,5 L0,10 Z"></path></marker>
E         ?                                                         ++++++++++++++++++

tests/test_svg.py:178: AssertionError
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
E       assert '<svg width="...xt></g></svg>' == '<svg xmlns="...xt></g></svg>'
E         
E         - <svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 100 100"><defs><linearGradient id="grad1"><stop offset="0%" stop-color="red"></stop><stop offset="100%" stop-color="blue"></stop></linearGradient></defs><g class="main-content"><circle cx="50" cy="50" r="40" style="fill: url(#grad1);"></circle><text x="35" y="55" style="font-family: Arial;">SVG</text></g></svg>
E         ?                                        -----------------------------------------------
E         + <svg width="100" height="100" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><defs><...
E         
E         ...Full output truncated (2 lines hidden), use '-vv' to show

tests/test_svg.py:218: AssertionError
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
E       assert '<image fetch...ous"></image>' == '<image x="10...igh"></image>'
E         
E         - <image x="10" y="20" width="100" height="80" href="image.jpg" crossorigin="anonymous" fetchpriority="high"></image>
E         + <image fetchpriority="high" href="image.jpg" x="10" y="20" width="100" height="80" crossorigin="anonymous"></image>

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
E       assert '<script fetc...ls"></script>' == '<script type...ow"></script>'
E         
E         - <script type="application/javascript" href="script.js" crossorigin="use-credentials" fetchpriority="low"></script>
E         + <script fetchpriority="low" href="script.js" type="application/javascript" crossorigin="use-credentials"></script>

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
E       assert '<animate att...s"></animate>' == '<animate att...r"></animate>'
E         
E         - <animate attributeName="opacity" attributeType="CSS" dur="2s" repeatCount="3" repeatDur="10s" from-="0" to="1" by="0.5" begin="1s" end="5s" calcMode="linear"></animate>
E         + <animate attributeType="CSS" attributeName="opacity" from="0" to="1" by="0.5" calcMode="linear" begin="1s" dur="2s" end="5s" repeatCount="3" repeatDur="10s"></animate>

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
PASSED tests/test_svg.py::test_rect_with_all_attributes
PASSED tests/test_svg.py::test_ellipse_coordinates
PASSED tests/test_svg.py::test_line_coordinates
PASSED tests/test_svg.py::test_path_with_data
PASSED tests/test_svg.py::test_svg_with_viewbox
PASSED tests/test_svg.py::test_group_with_children
PASSED tests/test_svg.py::test_text_with_positioning
PASSED tests/test_svg.py::test_tspan_in_text
PASSED tests/test_svg.py::test_linear_gradient_with_stops
PASSED tests/test_svg.py::test_radial_gradient
PASSED tests/test_svg.py::test_fe_distant_light
PASSED tests/test_svg.py::test_fe_drop_shadow
PASSED tests/test_svg.py::test_animate_with_values
PASSED tests/test_svg.py::test_animate_motion_with_path
PASSED tests/test_svg.py::test_mask_with_content
PASSED tests/test_svg.py::test_none_attributes_filtered
PASSED tests/test_svg.py::test_mixed_type_attributes
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
FAILED tests/test_svg.py::test_filter_with_effects - assert '<filter x="-...s...
FAILED tests/test_svg.py::test_marker_definition - assert '<marker mark...ath...
FAILED tests/test_svg.py::test_complex_svg_structure - assert '<svg width=".....
FAILED tests/test_svg.py::test_image_with_experimental_attributes - assert '<...
FAILED tests/test_svg.py::test_script_with_experimental_attributes - assert '...
FAILED tests/test_svg.py::test_animate_with_extended_attributes - assert '<an...
========================= 8 failed, 88 passed in 0.46s =========================
