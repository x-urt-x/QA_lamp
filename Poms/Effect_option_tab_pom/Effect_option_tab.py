from playwright.sync_api import Page, expect

from Poms.Effect_option_tab_pom.Blocks.Base_effect_block import BaseEffectBlock
from Poms.Effect_option_tab_pom.Blocks.Color_effect_block import ColorEffectBlock
from Poms.Effect_option_tab_pom.Blocks.Preset_effect_block import PresetEffectBlock
from Poms.Effect_option_tab_pom.Blocks.Rainbow_effect_block import RainbowEffectBlock


class EffectOptionTab:
    def __init__(self, root, page):

        self._page = page
        self._root = root
        self._currentEffect_root = self._root.locator("#currentEffect")

        self._effect_selector = self._root.locator("#effect-selector")

        self._reset_option_button = self._root.get_by_role("button", name="Reset option")
        self._apply_all_button = self._root.get_by_role("button", name="Apply all")
        self._reload_button = self._root.get_by_role("button", name="🗘")

    def select_effect_by_label(self, label: str):
        self._effect_selector.select_option(label=label)

    def select_effect_by_value(self, value: int):
        self._effect_selector.select_option(value=str(value))

    def reset_option(self):
        self._reset_option_button.click()

    def apply_all(self):
        self._apply_all_button.click()

    def reload(self):
        self._reload_button.click()

    def block_root(self, name: str):
        return self._currentEffect_root.locator(".effect-block").filter(
            has=self._page.locator("p.name", has_text=name)
        )

    def base_block(self):
        return BaseEffectBlock(self.block_root("Base"))

    def color_block(self):
        return ColorEffectBlock(self.block_root("Color"))

    def preset_block(self):
        return PresetEffectBlock(self.block_root("Preset"))

    def rainbow_block(self):
        return RainbowEffectBlock(self.block_root("Rainbow"))

    def expect_visible(self):
        expect(self._root).to_be_visible()

    def expect_hidden(self):
        expect(self._root).to_be_hidden()