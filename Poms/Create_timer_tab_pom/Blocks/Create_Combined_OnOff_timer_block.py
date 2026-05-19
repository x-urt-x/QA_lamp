from Poms.Create_timer_tab_pom.Blocks.Create_timer_block_base import CreateTimerBlockBase


class CreateCombinedOnOffTimerBlock(CreateTimerBlockBase):
    def __init__(self, root):
        super().__init__(root)

        self._duration_input = root.locator(
            'input[name="dur"]'
        )

        self._delay_input = root.locator(
            'input[name="delay"]'
        )

        self._final_brightness_input = root.locator(
            'input[name="to_br"]'
        )

        self._turn_off_on_end_checkbox = root.locator(
            'input[name="end_set"]'
        )

        self._start_brightness_input = root.locator(
            'input[name="from_br"]'
        )

        self._turn_on_on_start_checkbox = root.locator(
            'input[name="start_set"]'
        )

    def set_duration(self, value: int):
        self._duration_input.fill(str(value))

    def set_delay(self, value: int):
        self._delay_input.fill(str(value))

    def set_final_brightness(self, value: int):
        self._final_brightness_input.fill(str(value))

    def set_turn_off_on_end(self, state: bool):
        self._turn_off_on_end_checkbox.set_checked(state)

    def set_start_brightness(self, value: int):
        self._start_brightness_input.fill(str(value))

    def set_turn_on_on_start(self, state: bool):
        self._turn_on_on_start_checkbox.set_checked(state)