from playwright.sync_api import expect
from Poms.Mem_timers_pom.timers.Mem_timer_block_base import MemTimerBlockBase

class OnOffMemTimerBlock(MemTimerBlockBase):
    def __init__(self, root):
        super().__init__(root)

        self.change_state_checkbox = root.locator(
            'input[name="to_set"]'
        )

    def expect_change_state(self, state: bool):
        if state:
            expect(self.change_state_checkbox).to_be_checked()
        else:
            expect(self.change_state_checkbox).not_to_be_checked()