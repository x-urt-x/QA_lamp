from Poms.Create_timer_tab_pom.Blocks.Create_timer_block_base import CreateTimerBlockBase


class CreateOnOffTimerBlock(CreateTimerBlockBase):
    def __init__(self, root):
        super().__init__(root)

        self.change_state_checkbox = root.locator(
            'input[name="to_set"]'
        )

    def set_change_state(self, state: bool):
        self.change_state_checkbox.set_checked(state)