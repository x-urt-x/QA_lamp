from playwright.sync_api import Page, expect


class BaseEffectBlock:
    def __init__(self, root):
        self._root = root

        self._auto_send_checkbox = root.locator("input.auto-send-toggle")

        self._delay_input = root.locator(
            'input[name="strip_update_delay_time"]'
        )

        self._cutoff_bound_input = root.locator(
            'input[name="br_cutoff_bound"]'
        )

        self._effect_step_input = root.locator(
            'input[name="effect_step"]'
        )

    def set_auto_send(self, state: bool):
        self._auto_send_checkbox.set_checked(state, force=True)

    def set_delay(self, value: int):
        self._delay_input.fill(str(value))

    def expect_delay(self, value: int):
        expect(self._delay_input).to_have_value(str(value))

    def set_cutoff_bound(self, value: int):
        self._cutoff_bound_input.fill(str(value))

    def expect_cutoff_bound(self, value: int):
        expect(self._cutoff_bound_input).to_have_value(str(value))

    def set_effect_step(self, value: int):
        self._effect_step_input.fill(str(value))

    def expect_effect_step(self, value: int):
        expect(self._effect_step_input).to_have_value(str(value))
