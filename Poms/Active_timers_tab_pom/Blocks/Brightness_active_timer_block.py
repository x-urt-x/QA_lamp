from playwright.sync_api import expect
from Poms.Active_timers_tab_pom.Blocks.Active_timer_block_base import ActiveTimerBlockBase


class BrightnessActiveTimerBlock(ActiveTimerBlockBase):
    def __init__(self, root):
        super().__init__(root)

        self.remaining_steps_input = root.locator(
            'input[name="step_counter"]'
        )

        self.final_brightness_input = root.locator(
            'input[name="to_br"]'
        )

    def expect_remaining_steps(self, value: int):
        expect(self.remaining_steps_input).to_have_value(str(value))

    def expect_final_brightness(self, value: int):
        expect(self.final_brightness_input).to_have_value(str(value))