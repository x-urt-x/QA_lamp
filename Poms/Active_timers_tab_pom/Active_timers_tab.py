from Poms.Active_timers_tab_pom.Blocks.Brightness_active_timer_block import BrightnessActiveTimerBlock
from Poms.Active_timers_tab_pom.Blocks.Clock_active_timer_block import ClockActiveTimerBlock
from Poms.Active_timers_tab_pom.Blocks.Command_active_timer_block import CommandActiveTimerBlock
from Poms.Active_timers_tab_pom.Blocks.Main_active_timer_block import MainActiveTimerBlock
from Poms.Active_timers_tab_pom.Blocks.OnOff_active_timer_block import OnOffActiveTimerBlock


class ActiveTimersTab:
    def __init__(self, page):
        self.page = page

        self.root = page.locator("#activeTimersContainer")
        self.activeTimers_root = self.root.locator("#activeTimers")

        self.reload_button = self.root.get_by_role("button", name="🗘")

    def reload(self):
        self.reload_button.click()

    def timer_root(self, name: str):
        return self.activeTimers_root.locator(".active-timer-block").filter(
            has=self.page.locator("p.name", has_text=name)
        )

    def main_timer(self):
        return MainActiveTimerBlock(self.timer_root("Main timer"))

    def clock_timer(self):
        return ClockActiveTimerBlock(self.timer_root("Clock timer"))

    def command_timer(self):
        return CommandActiveTimerBlock(self.timer_root("Command timer"))

    def brightness_timer(self):
        return BrightnessActiveTimerBlock(self.timer_root("Brightness timer"))

    def on_off_timer(self):
        return OnOffActiveTimerBlock(self.timer_root("OnOff timer"))