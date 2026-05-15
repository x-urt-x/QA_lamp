from playwright.sync_api import Page

from Poms.Mem_timers_pom.timers.Command_mem_timer_block import CommandMemTimerBlock


class MemTimerTab:
    def __init__(self, page: Page):
        self.page = page

        self.root = page.locator("#memTimersContainer")
        self.memTimers_root = self.root.locator("#memTimers")

        self.reload_button = self.root.locator(
            'button[onclick="loadTimers()"]'
        )

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