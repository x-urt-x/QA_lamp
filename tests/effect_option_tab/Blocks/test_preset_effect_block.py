from playwright.sync_api import Page

from Poms.Main_page import MainPage


def test_select_preset_red_fire(page: Page):
    main_page = MainPage(page)
    main_page.open_page()

    main_page.open_effect_option_tab()
    main_page.effect_option_tab.select_effect_by_label("Fire")
    preset = main_page.effect_option_tab.preset_block()

    with main_page.expect_submit_request() as request_info:
        preset.select("red fire")

    request = request_info.value
    assert request.method == "POST"
    assert "ep 0" in (request.post_data or "")