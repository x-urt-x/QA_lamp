from playwright.sync_api import expect


class ActiveTimerBlockBase:
    def __init__(self, root):
        self._root = root

        self._is_active_checkbox = root.locator(
            'input[name="is_active"]'
        )

        self._prev_time_input = root.locator(
            'input[name="prev_time"]'
        )

        self._delay_input = root.locator(
            'input[name="delay"]'
        )

        self._addr_input = root.locator(
            'input[name="addr"]'
        )

        self._delete_button = root.locator(
            "button.active-timer-button-delete"
        )

    def expect_is_active(self, state: bool):
        if state:
            expect(self._is_active_checkbox).to_be_checked()
        else:
            expect(self._is_active_checkbox).not_to_be_checked()

    def expect_prev_time(self, value: int):
        expect(self._prev_time_input).to_have_value(str(value))

    def expect_delay(self, value: int):
        expect(self._delay_input).to_have_value(str(value))

    def expect_addr(self, value: int):
        expect(self._addr_input).to_have_value(str(value))

    def delete(self):
        self._delete_button.click()

class NotDeletableActiveTimerBlockBase(ActiveTimerBlockBase):
    def delete(self):
        raise RuntimeError("This active timer cannot be deleted")