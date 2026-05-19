from Poms.Create_timer_tab_pom.Blocks.Create_timer_block_base import CreateTimerBlockBase


class CreateCommandTimerBlock(CreateTimerBlockBase):
    def __init__(self, root):
        super().__init__(root)

        self._delay_input = root.locator(
            'input[name="delay"]'
        )

        self._once_checkbox = root.locator(
            'input[name="once"]'
        )

        self._command_input = root.locator(
            'input[name="command"]'
        )

    def set_delay(self, value: int):
        self._delay_input.fill(str(value))

    def set_once(self, state: bool):
        self._once_checkbox.set_checked(state)

    def set_command(self, value: str):
        self._command_input.fill(value)