from playwright.sync_api import Page, expect


class ColorEffectBlock:
    def __init__(self, root):
        self._root = root

        self._auto_send_checkbox = root.locator(
            "input.auto-send-toggle"
        )

        self._color_inputs = root.locator(
            'input[type="color"]'
        )

    def set_auto_send(self, state: bool):
        self._auto_send_checkbox.set_checked(state, force=True)

    def set_color(self, index: int, value: str):
        self._color_inputs.nth(index).fill(value)

    def expect_color(self, index: int, value: str):
        expect(
            self._color_inputs.nth(index)
        ).to_have_value(value)