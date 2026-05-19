from playwright.sync_api import expect


class PresetEffectBlock:
    def __init__(self, root):
        self._root = root

        self._preset_buttons = root.locator(
            'button[command="ep"]'
        )

    def _preset_button(self, name: str):
        return

    def select(self, name: str):
        self._root.get_by_role(
            "button",
            name=name
        ).click()
