from playwright.sync_api import expect


class StaticFields:
    def __init__(self, root):
        self._root = root

        self._state_toggle_checkbox = root.locator(
            "#state-toggle"
        )

        self._brightness_knob = root.locator(
            "#brKnob"
        )

        self._brightness_input = root.locator(
            "#brInput"
        )

        self._udp_checkbox = root.locator(
            "#UDP"
        )

        self._brightness_limit_input = root.locator(
            "#brLimit"
        )

        self._apply_and_save_button = root.get_by_role(
            "button",
            name="apply & save",
            exact=True
        )

        self._apply_button = root.get_by_role(
            "button",
            name="apply",
            exact = True
        )

    def set_state(self, state: bool):
        self._state_toggle_checkbox.set_checked(state, force=True)

    def expect_state(self, state: bool):
        if state:
            expect(self._state_toggle_checkbox).to_be_checked()
        else:
            expect(self._state_toggle_checkbox).not_to_be_checked()

    def set_brightness(self, value: int):
        self._brightness_input.fill(str(value))
        self._brightness_input.press("Enter")

    def expect_brightness(self, value: int):
        expect(
            self._brightness_input
        ).to_have_value(str(value))

    def set_udp(self, state: bool):
        self._udp_checkbox.set_checked(state, force=True)

    def expect_udp(self, state: bool):
        if state:
            expect(self._udp_checkbox).to_be_checked()
        else:
            expect(self._udp_checkbox).not_to_be_checked()

    def set_brightness_limit(self, value: int):
        self._brightness_limit_input.fill(str(value))

    def expect_brightness_limit(self, value: int):
        expect(
            self._brightness_limit_input
        ).to_have_value(str(value))

    def apply_brightness_limit(self):
        self._apply_button.click()

    def apply_and_save_brightness_limit(self):
        self._apply_and_save_button.click()