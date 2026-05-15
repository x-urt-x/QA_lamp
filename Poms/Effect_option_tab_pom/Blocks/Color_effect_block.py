from playwright.sync_api import Page, expect


class ColorEffectBlock:
    def __init__(self, root):
        self.root = root

        self.auto_send_checkbox = root.locator(
            "input.auto-send-toggle"
        )

        self.color_inputs = root.locator(
            'input[type="color"]'
        )

    def set_auto_send(self, state: bool):
        self.auto_send_checkbox.set_checked(state)

    def set_color(self, index: int, value: str):
        self.color_inputs.nth(index).fill(value)

    def expect_color(self, index: int, value: str):
        expect(
            self.color_inputs.nth(index)
        ).to_have_value(value)