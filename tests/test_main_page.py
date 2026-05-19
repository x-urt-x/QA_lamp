import pytest
from playwright.sync_api import Page
from Poms.Main_page import MainPage

def test_send_command(page: Page):
    main_page = MainPage(page)
    main_page.open_page()
    with main_page.expect_submit_request() as request_info:
        main_page.send_command("test command")

    request = request_info.value

    assert request.method == "POST"
    assert request.post_data == "test command"

def test_default_tab(page: Page):
    main_page = MainPage(page)
    main_page.open_page()

    main_page.effect_option_tab.expect_visible()
    main_page.mem_timer_tab.expect_hidden()
    main_page.active_timer_tab.expect_hidden()
    main_page.create_timer_tab.expect_hidden()

@pytest.mark.parametrize(
    "open_method, visible_tab",
    [
        ("open_effect_option_tab", "effect_option_tab"),
        ("open_mem_timer_tab", "mem_timer_tab"),
        ("open_active_timer_tab", "active_timer_tab"),
        ("open_create_timer_tab", "create_timer_tab"),
    ]
)
def test_only_one_tab_visible(page, open_method, visible_tab):
    main_page = MainPage(page)
    main_page.open_page()

    getattr(main_page, open_method)()

    tabs = {
        "effect_option_tab": main_page.effect_option_tab,
        "mem_timer_tab": main_page.mem_timer_tab,
        "active_timer_tab": main_page.active_timer_tab,
        "create_timer_tab": main_page.create_timer_tab,
    }

    for tab_name, tab in tabs.items():
        if tab_name == visible_tab:
            tab.expect_visible()
        else:
            tab.expect_hidden()
