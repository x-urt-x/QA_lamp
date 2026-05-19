from playwright.sync_api import expect

from Poms.Active_timers_tab_pom.Blocks.Brightness_active_timer_block import BrightnessActiveTimerBlock
from Poms.Active_timers_tab_pom.Blocks.Clock_active_timer_block import ClockActiveTimerBlock
from Poms.Active_timers_tab_pom.Blocks.Command_active_timer_block import CommandActiveTimerBlock
from Poms.Active_timers_tab_pom.Blocks.Main_active_timer_block import MainActiveTimerBlock
from Poms.Active_timers_tab_pom.Blocks.OnOff_active_timer_block import OnOffActiveTimerBlock


class ActiveTimersTab:
    def __init__(self, root):

        self._root = root
        self._activeTimers_root = self._root.locator("#activeTimers")

        self._reload_button = self._root.get_by_role("button", name="🗘")

    def reload(self):
        self._reload_button.click()

    def timer_root(self, name: str):
        return self._activeTimers_root.locator(".active-timer-block").filter(
            has=self._root.locator("p.name", has_text=name)
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

    def expect_visible(self):
        expect(self._root).to_be_visible()

    def expect_hidden(self):
        expect(self._root).to_be_hidden()