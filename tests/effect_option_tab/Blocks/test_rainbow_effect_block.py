from playwright.sync_api import Page

from Poms.Main_page import MainPage


def test_rainbow_enabled(page: Page):
    main_page = MainPage(page)
    main_page.open_page()

    main_page.open_effect_option_tab()
    main_page.effect_option_tab.select_effect_by_label("Single Color")
    rainbow = main_page.effect_option_tab.rainbow_block()

    rainbow.set_auto_send(1)

    with main_page.expect_submit_request() as request_info:
        rainbow.set_rainbow_enabled(0, 1)

    request = request_info.value
    assert request.method == "POST"
    assert "ers 0 1" in (request.post_data or "")

    rainbow.expect_rainbow_enabled(0, 1)

def test_rainbow_step(page: Page):
    main_page = MainPage(page)
    main_page.open_page()

    main_page.open_effect_option_tab()
    main_page.effect_option_tab.select_effect_by_label("Single Color")
    rainbow = main_page.effect_option_tab.rainbow_block()

    rainbow.set_auto_send(1)

    with main_page.expect_submit_request() as request_info:
        rainbow.set_rainbow_step(0, 10)

    request = request_info.value
    assert request.method == "POST"
    assert "erh 0 10" in (request.post_data or "")

    rainbow.expect_rainbow_step(0, 10)