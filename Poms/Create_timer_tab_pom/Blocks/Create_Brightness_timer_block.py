from Poms.Create_timer_tab_pom.Blocks.Create_timer_block_base import CreateTimerBlockBase


class CreateBrightnessTimerBlock(CreateTimerBlockBase):
    def __init__(self, root):
        super().__init__(root)

        self.delay_input = root.locator(
            'input[name="delay"]'
        )

        self.duration_input = root.locator(
            'input[name="dur"]'
        )

        self.final_brightness_input = root.locator(
            'input[name="to_br"]'
        )

    def set_delay(self, value: int):
        self.delay_input.fill(str(value))

    def set_duration(self, value: int):
        self.duration_input.fill(str(value))

    def set_final_brightness(self, value: int):
        self.final_brightness_input.fill(str(value))