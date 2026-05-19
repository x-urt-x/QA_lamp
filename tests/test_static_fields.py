import pytest
from playwright.sync_api import Page
from Poms.Main_page import MainPage
from Poms.Static_fields import StaticFields


@pytest.mark.parametrize(
    "target_state, expected_command",
    [
        (True, "ts 0 1"),
        (False, "ts 0 0")
    ]
)
def test_on_off_toggle(page: Page, target_state, expected_command):
    main_page = MainPage(page)
    main_page.open_page()

    main_page.wait_effect_option_data()

    static_fields: StaticFields = main_page.static_fields

    static_fields.set_state(not target_state)

    with main_page.expect_submit_request() as request_info:
        static_fields.set_state(target_state)

    request = request_info.value

    assert request.method == "POST"
    assert expected_command in (request.post_data or "")

    main_page.open_effect_option_tab()
    main_page.effect_option_tab.reload()

    static_fields.expect_state(target_state)


@pytest.mark.parametrize(
    "target_state, expected_command",
    [
        (True, "mu 1"),
        (False, "mu 0")
    ]
)
def test_UDP_toggle(page: Page, target_state, expected_command):
    main_page = MainPage(page)
    main_page.open_page()

    main_page.wait_effect_option_data()

    static_fields: StaticFields = main_page.static_fields

    static_fields.set_udp(not target_state)

    with main_page.expect_submit_request() as request_info:
        static_fields.set_udp(target_state)

    request = request_info.value

    assert request.method == "POST"
    assert expected_command in (request.post_data or "")

    main_page.effect_option_tab.reload()

    static_fields.expect_udp(target_state)


@pytest.mark.parametrize(
    "value_builder, expected_after_reload_builder",
    [
        (
            lambda max_br: -1000,
            lambda max_br: 0,
        ),
        (
            lambda max_br: 0,
            lambda max_br: 0,
        ),
        (
            lambda max_br: max_br // 2,
            lambda max_br: max_br // 2,
        ),
        (
            lambda max_br: max_br,
            lambda max_br: max_br,
        ),
        (
            lambda max_br: max_br + 1000,
            lambda max_br: max_br,
        ),
    ]
)
def test_set_brightness_input(
    page: Page,
    value_builder,
    expected_after_reload_builder
):
    main_page = MainPage(page)
    main_page.open_page()

    main_page.wait_effect_option_data()

    static_fields = main_page.static_fields

    max_br = main_page.max_brightness

    saved_max_br = None
    if max_br == 0:
        saved_max_br = max_br
        static_fields.set_brightness_limit(100)
        static_fields.apply_brightness_limit()
        max_br = 100

    static_fields.set_brightness(1)

    input_value = value_builder(max_br)
    expected_after_reload = expected_after_reload_builder(max_br)

    with main_page.expect_submit_request() as request_info:
        static_fields.set_brightness(input_value)

    request = request_info.value

    assert request.method == "POST"
    assert f"mb {input_value}" in (request.post_data or "")

    static_fields.expect_brightness(input_value)

    main_page.open_effect_option_tab()
    main_page.effect_option_tab.reload()

    static_fields.expect_brightness(expected_after_reload)

    if saved_max_br:
        static_fields.set_brightness_limit(saved_max_br)
        static_fields.apply_brightness_limit()


@pytest.mark.parametrize(
    "value_builder, expected_after_reload_builder",
    [
        (
            lambda br_limit: -1000,
            lambda br_limit: 0,
        ),
        (
            lambda br_limit: 0,
            lambda br_limit: 0,
        ),
        (
            lambda br_limit: br_limit // 2,
            lambda br_limit: br_limit // 2,
        ),
        (
            lambda br_limit: br_limit,
            lambda br_limit: br_limit,
        ),
        (
            lambda br_limit: br_limit + 1000,
            lambda br_limit: br_limit,
        ),
    ]
)
def test_apply_brightness_limit(
    page: Page,
    value_builder,
    expected_after_reload_builder
):
    main_page = MainPage(page)
    main_page.open_page()

    main_page.wait_effect_option_data()

    main_page.wait_effect_option_data()

    static_fields = main_page.static_fields

    br_limit = main_page.max_brightness
    input_value = value_builder(br_limit)
    expected_after_reload = expected_after_reload_builder(br_limit)

    static_fields.set_brightness_limit(input_value)
    static_fields.expect_brightness_limit(input_value)

    with main_page.expect_submit_request() as request_info:
        static_fields.apply_brightness_limit()

    request = request_info.value

    assert request.method == "POST"
    assert f"ml 0 {input_value}" in (request.post_data or "")

    main_page.open_effect_option_tab()
    main_page.effect_option_tab.reload()

    static_fields.expect_brightness_limit(expected_after_reload)


def test_apply_and_save_brightness_limit_sends_command(page: Page):
    main_page = MainPage(page)
    main_page.open_page()

    static_fields = main_page.static_fields

    page.route(
        main_page._SUBMIT_ENDPOINT,
        lambda route: route.fulfill(
            status=200,
        )
    )

    static_fields.set_brightness_limit(1000)

    with main_page.expect_submit_request() as request_info:
        static_fields.apply_and_save_brightness_limit()

    request = request_info.value

    assert request.method == "POST"
    assert "ml 1 1000" in (request.post_data or "")