from playwright.sync_api import expect
from Poms.Mem_timers_tab_pom.Blocks.Mem_timer_block_base import MemTimerBlockBase


class CommandMemTimerBlock(MemTimerBlockBase):
    def __init__(self, root):
        super().__init__(root)

        self.delay_input = root.locator(
            'input[name="delay"]'
        )

        self.once_checkbox = root.locator(
            'input[name="once"]'
        )

        self.command_input = root.locator(
            'input[name="command"]'
        )

    def expect_delay(self, value: int):
        expect(self.delay_input).to_have_value(str(value))

    def expect_once(self, state: bool):
        if state:
            expect(self.once_checkbox).to_be_checked()
        else:
            expect(self.once_checkbox).not_to_be_checked()

    def expect_command(self, value: str):
        expect(self.command_input).to_have_value(value)