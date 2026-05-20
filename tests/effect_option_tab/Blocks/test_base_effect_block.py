from playwright.sync_api import Page

from Poms.Main_page import MainPage


def test_base_effect_delay(page: Page):
    main_page = MainPage(page)
    main_page.open_page()

    main_page.open_effect_option_tab()
    base = main_page.effect_option_tab.base_block()

    base.set_auto_send(1)

    with main_page.expect_submit_request() as request_info:
        base.set_delay(100)

    request = request_info.value
    assert request.method == "POST"
    assert "ebd 100" in (request.post_data or "")

    base.expect_delay(100)

def test_base_effect_cutoff_bound(page: Page):
    main_page = MainPage(page)
    main_page.open_page()

    main_page.open_effect_option_tab()
    base = main_page.effect_option_tab.base_block()

    base.set_auto_send(1)

    with main_page.expect_submit_request() as request_info:
        base.set_cutoff_bound(50)

    request = request_info.value
    assert request.method == "POST"
    assert "ebc 50" in (request.post_data or "")

    base.expect_cutoff_bound(50)

def test_base_effect_step(page: Page):
    main_page = MainPage(page)
    main_page.open_page()

    main_page.open_effect_option_tab()
    base = main_page.effect_option_tab.base_block()

    base.set_auto_send(1)

    with main_page.expect_submit_request() as request_info:
        base.set_effect_step(5)

    request = request_info.value
    assert request.method == "POST"
    assert "ebh 5" in (request.post_data or "")

    base.expect_effect_step(5)