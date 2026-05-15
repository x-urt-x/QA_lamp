from playwright.sync_api import expect


class PresetEffectBlock:
    def __init__(self, root):
        self.root = root

    def select(self, name: str):
        self.root.get_by_role(
            "button",
            name=name
        ).click()

    def expect_preset_visible(self, name: str):
        expect(
            self.root.get_by_role(
                "button",
                name=name
            )
        ).to_be_visible()