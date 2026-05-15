from playwright.sync_api import Page, expect
from Poms.Effect_option_tab_pom.Effect_option_tab import EffectOptionTab
from Poms.Static_fields import StaticFields


class MainPage:
    def __init__(self, page: Page):
        self.page = page
        self._effect_option_tab = EffectOptionTab(self.page)
        self.static_fields = StaticFields(self.page)

        self.command_console_input = page.locator(
            "#commandConsole"
        )

        self.send_command_button = page.get_by_role(
            "button",
            name="send to /submit"
        )

    def open_effect_option(self, page: Page):
        page.get_by_role("button", name="Effect options").click()
        return self._effect_option_tab

    def send_command(self, command: str):
        self.command_console_input.fill(command)
        self.send_command_button.click()