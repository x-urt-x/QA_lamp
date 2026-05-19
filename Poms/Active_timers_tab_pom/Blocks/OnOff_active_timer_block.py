from playwright.sync_api import expect
from Poms.Active_timers_tab_pom.Blocks.Active_timer_block_base import ActiveTimerBlockBase


class OnOffActiveTimerBlock(ActiveTimerBlockBase):
    def __init__(self, root):
        super().__init__(root)

        self._change_state_checkbox = root.locator(
            'input[name="to_set"]'
        )

    def expect_change_state(self, state: bool):
        if state:
            expect(self._change_state_checkbox).to_be_checked()
        else:
            expect(self._change_state_checkbox).not_to_be_checked()