import pytest
from playwright.sync_api import Page
from Poms.Main_page import MainPage
from Poms.Effect_option_tab_pom.Effect_option_tab import EffectOptionTab

@pytest.mark.parametrize(
    "effect_name",
    [
        "Single Color",
        "Fire",
        "Rainbow Wave",
        "Noise"
    ]
)
def test_effect_selector(page: Page, effect_name):
    main_page = MainPage(page)
    main_page.open_page()

    main_page.open_effect_option_tab()
    tab: EffectOptionTab = main_page.effect_option_tab

    tab.select_effect_by_label(effect_name)
    main_page.effect_option_data = None
    main_page.wait_effect_option_data()
    assert main_page.current_effect == effect_name

def test_reset_effect_option_sends_command(page: Page):
    main_page = MainPage(page)
    main_page.open_page()

    effect_tab = main_page.open_effect_option_tab()

    with main_page.expect_submit_request() as request_info:
        effect_tab.reset_option()

    request = request_info.value
    assert request.method == "POST"
    assert "md" in (request.post_data or "")

def test_apply_all_sends_all_effect_blocks(page: Page):
    main_page = MainPage(page)
    main_page.open_page()

    main_page.open_effect_option_tab()
    tab = main_page.effect_option_tab
    tab.select_effect_by_label("Single Color")

    base = tab.base_block()
    color = tab.color_block()
    rainbow = tab.rainbow_block()

    base.set_delay(100)
    color.set_color(0, "#ff0000")
    rainbow.set_rainbow_step(0, 10)

    with main_page.expect_submit_request() as request_info:
        tab.apply_all()

    request = request_info.value
    body = request.post_data or ""

    assert request.method == "POST"
    assert "ebd 100" in body
    assert "ec 0 ff0000" in body
    assert "erh 0 10" in body