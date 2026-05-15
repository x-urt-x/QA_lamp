from Poms.Active_timers_tab_pom.Active_timers_tab import ActiveTimersTab
from Poms.Create_timer_tab_pom.Create_timer_tab import CreateTimerTab
from Poms.Effect_option_tab_pom.Effect_option_tab import EffectOptionTab
from Poms.Mem_timers_tab_pom.Mem_timers_tab import MemTimersTab
from Poms.Static_fields import StaticFields


class MainPage:
    def __init__(self, page):
        self.page = page

        self.command_console_input = page.locator(
            "#commandConsole"
        )

        self.send_command_button = page.get_by_role(
            "button",
            name="send to /submit"
        )

        self.effect_options_tab_button = page.get_by_role(
            "button",
            name="Effect options"
        )

        self.mem_timers_tab_button = page.get_by_role(
            "button",
            name="Mem timers"
        )

        self.active_timers_tab_button = page.get_by_role(
            "button",
            name="Active timers"
        )

        self.create_timer_tab_button = page.get_by_role(
            "button",
            name="Create timer"
        )

        self.effect_option_tab = EffectOptionTab(page)
        self.mem_timer_tab = MemTimersTab(page)
        self.active_timer_tab = ActiveTimersTab(page)
        self.create_timer_tab = CreateTimerTab(page)

        self.static_fields = StaticFields(page)

    def send_command(self, command: str):
        self.command_console_input.fill(command)
        self.send_command_button.click()

    def open_effect_option_tab(self):
        self.effect_options_tab_button.click()
        return self.effect_option_tab

    def open_mem_timer_tab(self):
        self.mem_timers_tab_button.click()
        return self.mem_timer_tab

    def open_active_timer_tab(self):
        self.active_timers_tab_button.click()
        return self.active_timer_tab

    def open_create_timer_tab(self):
        self.create_timer_tab_button.click()
        return self.create_timer_tab