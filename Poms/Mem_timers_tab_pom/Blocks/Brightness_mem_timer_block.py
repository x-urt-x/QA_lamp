from playwright.sync_api import expect
from Poms.Mem_timers_tab_pom.Blocks.Mem_timer_block_base import MemTimerBlockBase


class BrightnessMemTimerBlock(MemTimerBlockBase):
    def __init__(self, root):
        super().__init__(root)

        self._delay_input = root.locator(
            'input[name="delay"]'
        )

        self._duration_input = root.locator(
            'input[name="dur"]'
        )

        self._final_brightness_input = root.locator(
            'input[name="to_br"]'
        )

    def expect_delay(self, value: int):
        expect(self._delay_input).to_have_value(str(value))

    def expect_duration(self, value: int):
        expect(self._duration_input).to_have_value(str(value))

    def expect_final_brightness(self, value: int):
        expect(self._final_brightness_input).to_have_value(str(value))