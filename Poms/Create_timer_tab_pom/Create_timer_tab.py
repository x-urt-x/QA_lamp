from playwright.sync_api import expect

from Poms.Create_timer_tab_pom.Blocks.Create_Brightness_timer_block import CreateBrightnessTimerBlock
from Poms.Create_timer_tab_pom.Blocks.Create_Combined_OnOff_timer_block import CreateCombinedOnOffTimerBlock
from Poms.Create_timer_tab_pom.Blocks.Create_Command_timet_block import CreateCommandTimerBlock
from Poms.Create_timer_tab_pom.Blocks.Create_OnOff_timer_block import CreateOnOffTimerBlock


class CreateTimerTab:
    def __init__(self, root):

        self._root = root
        self._createTimer_root = self._root.locator("#createTimer")

    def timer_root(self, name: str):
        return self._createTimer_root.locator(".mem-timer-block").filter(
            has=self._root.locator("p.name", has_text=name)
        ).first

    def brightness_timer(self):
        return CreateBrightnessTimerBlock(
            self.timer_root("Brightness timer")
        )

    def on_off_timer(self):
        return CreateOnOffTimerBlock(
            self.timer_root("OnOff timer")
        )

    def command_timer(self):
        return CreateCommandTimerBlock(
            self.timer_root("Command timer")
        )

    def combined_on_off_timer(self):
        return CreateCombinedOnOffTimerBlock(
            self.timer_root("Combined On Off timer")
        )

    def expect_visible(self):
        expect(self._root).to_be_visible()

    def expect_hidden(self):
        expect(self._root).to_be_hidden()