from playwright.sync_api import expect


class RainbowEffectBlock:
    def __init__(self, root):
        self._root = root

        self._auto_send_checkbox = root.locator(
            "input.auto-send-toggle"
        )

        self._rainbow_enable_checkboxes = root.locator(
            'input[name="rainbow-check"]'
        )

        self._rainbow_step_inputs = root.locator(
            'input[name="rainbow"]'
        )

    def set_auto_send(self, state: bool):
        self._auto_send_checkbox.set_checked(state, force=True)

    def set_rainbow_enabled(self, index: int, state: bool):
        self._rainbow_enable_checkboxes.nth(index).set_checked(state)

    def expect_rainbow_enabled(self, index: int, state: bool):
        checkbox = self._rainbow_enable_checkboxes.nth(index)

        if state:
            expect(checkbox).to_be_checked()
        else:
            expect(checkbox).not_to_be_checked()

    def set_rainbow_step(self, index: int, value: int):
        self._rainbow_step_inputs.nth(index).fill(str(value))

    def expect_rainbow_step(self, index: int, value: int):
        expect(
            self._rainbow_step_inputs.nth(index)
        ).to_have_value(str(value))