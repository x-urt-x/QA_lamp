from playwright.sync_api import Page

from Poms.Mem_timers_tab_pom.Blocks.Brightness_mem_timer_block import BrightnessMemTimerBlock
from Poms.Mem_timers_tab_pom.Blocks.Command_mem_timer_block import CommandMemTimerBlock
from Poms.Mem_timers_tab_pom.Blocks.OnOff_mem_timer_block import OnOffMemTimerBlock


class MemTimersTab:
    def __init__(self, page: Page):
        self.page = page

        self.root = page.locator("#memTimersContainer")
        self.memTimers_root = self.root.locator("#memTimers")

        self.reload_button = self.root.get_by_role("button", name="🗘")

    def reload(self):
        self.reload_button.click()

    def timer_root(self, name: str):
        return self.memTimers_root.locator(".mem-timer-block").filter(
            has=self.page.locator("p.name", has_text=name)
        )

    def command_timer(self):
        return CommandMemTimerBlock(self.timer_root("Command timer"))

    def brightness_timer(self):
        return BrightnessMemTimerBlock(self.timer_root("Brightness timer"))

    def on_off_timer(self):
        return OnOffMemTimerBlock(self.timer_root("OnOff timer"))