from playwright.sync_api import Page

from Poms.Effect_option_tab_pom.Blocks.Base_effect_block import BaseEffectBlock
from Poms.Effect_option_tab_pom.Blocks.Color_effect_block import ColorEffectBlock
from Poms.Effect_option_tab_pom.Blocks.Preset_effect_block import PresetEffectBlock
from Poms.Effect_option_tab_pom.Blocks.Rainbow_effect_block import RainbowEffectBlock


class EffectOptionTab:
    def __init__(self, page: Page):
        self.page = page

        self.root = page.locator("#effectContainer")
        self.currentEffect_root = self.root.locator("#currentEffect")

        self.effect_selector = self.root.locator("#effect-selector")

        self.reset_option_button = self.root.get_by_role("button", name="Reset option")
        self.apply_all_button = self.root.get_by_role("button", name="Apply all")
        self.reload_button = self.root.get_by_role("button", name="🗘")

    def select_effect_by_label(self, label: str):
        self.effect_selector.select_option(label=label)

    def select_effect_by_value(self, value: int):
        self.effect_selector.select_option(value=str(value))

    def reset_option(self):
        self.reset_option_button.click()

    def apply_all(self):
        self.apply_all_button.click()

    def reload(self):
        self.reload_button.click()

    def block_root(self, name: str):
        return self.currentEffect_root.locator(".effect-block").filter(
            has=self.page.locator("p.name", has_text=name)
        )

    def base_block(self):
        return BaseEffectBlock(self.block_root("Base"))

    def color_block(self):
        return ColorEffectBlock(self.block_root("Color"))

    def preset_block(self):
        return PresetEffectBlock(self.block_root("Preset"))

    def rainbow_block(self):
        return RainbowEffectBlock(self.block_root("Rainbow"))