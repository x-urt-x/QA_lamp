from playwright.sync_api import expect


class StaticFields:
    def __init__(self, root):
        self.root = root

        self.state_toggle_checkbox = root.locator(
            "#state-toggle"
        )

        self.brightness_knob = root.locator(
            "#brKnob"
        )

        self.brightness_input = root.locator(
            "#brInput"
        )

        self.udp_checkbox = root.locator(
            "#UDP"
        )

        self.brightness_limit_input = root.locator(
            "#brLimit"
        )

        self.apply_and_save_button = root.get_by_role(
            "button",
            name="apply & save"
        )

        self.apply_button = root.get_by_role(
            "button",
            name="apply"
        )

    def set_state(self, state: bool):
        self.state_toggle_checkbox.set_checked(state)

    def expect_state(self, state: bool):
        if state:
            expect(self.state_toggle_checkbox).to_be_checked()
        else:
            expect(self.state_toggle_checkbox).not_to_be_checked()

    def set_brightness(self, value: int):
        self.brightness_input.fill(str(value))

    def expect_brightness(self, value: int):
        expect(
            self.brightness_input
        ).to_have_value(str(value))

    def set_udp(self, state: bool):
        self.udp_checkbox.set_checked(state)

    def expect_udp(self, state: bool):
        if state:
            expect(self.udp_checkbox).to_be_checked()
        else:
            expect(self.udp_checkbox).not_to_be_checked()

    def set_brightness_limit(self, value: int):
        self.brightness_limit_input.fill(str(value))

    def expect_brightness_limit(self, value: int):
        expect(
            self.brightness_limit_input
        ).to_have_value(str(value))

    def apply_brightness_limit(self):
        self.apply_button.click()

    def apply_and_save_brightness_limit(self):
        self.apply_and_save_button.click()