from Poms.Create_timer_tab_pom.Blocks.Create_Brightness_timer_block import CreateBrightnessTimerBlock
from Poms.Create_timer_tab_pom.Blocks.Create_Combined_OnOff_timer_block import CreateCombinedOnOffTimerBlock
from Poms.Create_timer_tab_pom.Blocks.Create_Command_timet_block import CreateCommandTimerBlock
from Poms.Create_timer_tab_pom.Blocks.Create_OnOff_timer_block import CreateOnOffTimerBlock


class CreateTimerTab:
    def __init__(self, page):
        self.page = page

        self.root = page.locator("#createTimerContainer")
        self.createTimer_root = self.root.locator("#createTimer")

    def timer_root(self, name: str):
        return self.createTimer_root.locator(".mem-timer-block").filter(
            has=self.page.locator("p.name", has_text=name)
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