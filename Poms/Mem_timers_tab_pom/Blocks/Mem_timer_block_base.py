from playwright.sync_api import expect


class MemTimerBlockBase:
    def __init__(self, root):
        self.root = root

        self.active_on_create_checkbox = root.locator(
            'input[name="is_active"]'
        )

        self.week_day_checkboxes = root.locator(
            ".day-of-week input[type='checkbox']"
        )

        self.start_on_sec_input = root.locator(
            'input[name="timer_time_raw"]'
        )

        self.delete_button = root.locator(
            "button.mem-timer-button-delete"
        )

    def expect_active_on_create(self, state: bool):
        if state:
            expect(self.active_on_create_checkbox).to_be_checked()
        else:
            expect(self.active_on_create_checkbox).not_to_be_checked()

    def expect_week_day(self, index: int, state: bool):
        checkbox = self.week_day_checkboxes.nth(index)

        if state:
            expect(checkbox).to_be_checked()
        else:
            expect(checkbox).not_to_be_checked()

    def expect_start_on_sec(self, value: int):
        expect(self.start_on_sec_input).to_have_value(str(value))

    def delete(self):
        self.delete_button.click()