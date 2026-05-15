from playwright.sync_api import Page, expect


class BaseEffectBlock:
    def __init__(self, root):
        self.root = root

        self.auto_send_checkbox = root.locator("input.auto-send-toggle")

        self.delay_input = root.locator(
            'input[name="strip_update_delay_time"]'
        )

        self.cutoff_bound_input = root.locator(
            'input[name="br_cutoff_bound"]'
        )

        self.effect_step_input = root.locator(
            'input[name="effect_step"]'
        )

    def set_auto_send(self, state: bool):
        self.auto_send_checkbox.set_checked(state)

    def set_delay(self, value: int):
        self.delay_input.fill(str(value))

    def expect_delay(self, value: int):
        expect(self.delay_input).to_have_value(str(value))

    def set_cutoff_bound(self, value: int):
        self.cutoff_bound_input.fill(str(value))

    def expect_cutoff_bound(self, value: int):
        expect(self.cutoff_bound_input).to_have_value(str(value))

    def set_effect_step(self, value: int):
        self.effect_step_input.fill(str(value))

    def expect_effect_step(self, value: int):
        expect(self.effect_step_input).to_have_value(str(value))
