from playwright.sync_api import expect
from Poms.Active_timers_tab_pom.Blocks.Active_timer_block_base import ActiveTimerBlockBase


class CommandActiveTimerBlock(ActiveTimerBlockBase):
    def __init__(self, root):
        super().__init__(root)

        self._once_checkbox = root.locator(
            'input[name="once"]'
        )

        self._command_input = root.locator(
            'input[name="command"]'
        )

    def expect_once(self, state: bool):
        if state:
            expect(self._once_checkbox).to_be_checked()
        else:
            expect(self._once_checkbox).not_to_be_checked()

    def expect_command(self, value: str):
        expect(self._command_input).to_have_value(value)