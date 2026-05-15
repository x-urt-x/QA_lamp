class CreateTimerBlockBase:
    def __init__(self, root):
        self.root = root

        self.active_on_create_checkbox = root.locator(
            'input[name="is_active"]'
        )

        self.week_day_checkboxes = root.locator(
            ".day-of-week input[type='checkbox']"
        )

        self.timer_time_raw_input = root.locator(
            'input[name="timer_time_raw"]'
        )

        self.save_to_mem_checkbox = root.locator(
            "input.save-to-mem"
        )

        self.create_button = root.get_by_role(
            "button",
            name="create"
        )

    def set_active_on_create(self, state: bool):
        self.active_on_create_checkbox.set_checked(state)

    def set_week_day(self, index: int, state: bool):
        self.week_day_checkboxes.nth(index).set_checked(state)

    def set_timer_time_raw(self, value: int):
        self.timer_time_raw_input.fill(str(value))

    def set_save_to_mem(self, state: bool):
        self.save_to_mem_checkbox.set_checked(state)

    def create(self):
        self.create_button.click()