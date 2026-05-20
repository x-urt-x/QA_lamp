from playwright.sync_api import Page

from Poms.Main_page import MainPage


def test_color_effect_color_0(page: Page):
    main_page = MainPage(page)
    main_page.open_page()

    main_page.open_effect_option_tab()
    main_page.effect_option_tab.select_effect_by_label("Single Color")
    color = main_page.effect_option_tab.color_block()

    color.set_auto_send(1)

    with main_page.expect_submit_request() as request_info:
        color.set_color(0, "#ff0000")

    request = request_info.value
    assert request.method == "POST"
    assert "ec 0 ff0000" in (request.post_data or "")

    color.expect_color(0, "#ff0000")