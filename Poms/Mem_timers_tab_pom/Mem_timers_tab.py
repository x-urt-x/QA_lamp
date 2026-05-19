from playwright.sync_api import Page, expect

from Poms.Mem_timers_tab_pom.Blocks.Brightness_mem_timer_block import BrightnessMemTimerBlock
from Poms.Mem_timers_tab_pom.Blocks.Command_mem_timer_block import CommandMemTimerBlock
from Poms.Mem_timers_tab_pom.Blocks.OnOff_mem_timer_block import OnOffMemTimerBlock


class MemTimersTab:
    def __init__(self, root):

        self._root = root
        self._memTimers_root = self._root.locator("#memTimers")

        self._reload_button = self._root.get_by_role("button", name="🗘")

    def reload(self):
        self._reload_button.click()

    def timer_root(self, name: str):
        return self._memTimers_root.locator(".mem-timer-block").filter(
            has=self._root.locator("p.name", has_text=name)
        )

    def command_timer(self):
        return CommandMemTimerBlock(self.timer_root("Command timer"))

    def brightness_timer(self):
        return BrightnessMemTimerBlock(self.timer_root("Brightness timer"))

    def on_off_timer(self):
        return OnOffMemTimerBlock(self.timer_root("OnOff timer"))

    def expect_visible(self):
        expect(self._root).to_be_visible()

    def expect_hidden(self):
        expect(self._root).to_be_hidden()