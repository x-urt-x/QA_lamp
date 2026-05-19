import time

from Poms.Active_timers_tab_pom.Active_timers_tab import ActiveTimersTab
from Poms.Create_timer_tab_pom.Create_timer_tab import CreateTimerTab
from Poms.Effect_option_tab_pom.Effect_option_tab import EffectOptionTab
from Poms.Mem_timers_tab_pom.Mem_timers_tab import MemTimersTab
from Poms.Static_fields import StaticFields


class MainPage:
    _SUBMIT_ENDPOINT = "**/submit"
    _URL = "http://192.168.1.42/"
    _GET_EFFECT_OPTION_ENDPOINT = "**/get-effect-option"

    def __init__(self, page):
        self._page = page

        self._command_console_input = page.locator(
            "#commandConsole"
        )

        self._send_command_button = page.get_by_role(
            "button",
            name="send to /submit"
        )

        self._effect_options_tab_button = page.get_by_role(
            "button",
            name="Effect options"
        )

        self._mem_timers_tab_button = page.get_by_role(
            "button",
            name="Mem timers"
        )

        self._active_timers_tab_button = page.get_by_role(
            "button",
            name="Active timers"
        )

        self._create_timer_tab_button = page.get_by_role(
            "button",
            name="Create timer"
        )

        self._effectOptionContainer = page.locator("#effectContainer")
        self._memTimerContainer = page.locator("#memTimersContainer")
        self._activeTimerContainer = page.locator("#activeTimersContainer")
        self._createTimerContainer = page.locator("#createTimerContainer")

        self.effect_option_tab = EffectOptionTab(self._effectOptionContainer)
        self.mem_timer_tab = MemTimersTab(self._memTimerContainer)
        self.active_timer_tab = ActiveTimersTab(self._activeTimerContainer)
        self.create_timer_tab = CreateTimerTab(self._createTimerContainer)

        self.static_fields = StaticFields(page)

        self.effect_option_data = None
        self.max_brightness = None
        self.current_effect = None

        self._page.on(
            "response",
            self._handle_response
        )

    def _handle_response(self, response):
        if "/get-effect-option" not in response.url:
            return

        try:
            data = response.json()

            self.effect_option_data = data

            static_fields = data["staticFields"]

            self.max_brightness = static_fields["maxBr"]
            self.current_effect = static_fields["name"]

        except Exception:
            pass

    def open_page(self, retries: int = 3):
        for attempt in range(retries):
            try:
                self._page.goto(
                    self._URL,
                    wait_until="domcontentloaded",
                    timeout=5000
                )

                self._page.locator("#state-toggle").wait_for(
                    state="visible",
                    timeout=3000
                )

                return

            except TimeoutError:
                if attempt == retries - 1:
                    raise

                self._page.reload()
                self._page.wait_for_timeout(1000)

    def wait_effect_option_data(self, timeout_ms: int = 5000):
        start = time.monotonic()

        while self.effect_option_data is None:
            if (time.monotonic() - start) * 1000 > timeout_ms:
                raise TimeoutError(
                    "effect_option_data was not loaded"
                )

            self._page.wait_for_timeout(50)

    def send_command(self, command: str):
        self._command_console_input.fill(command)
        self._send_command_button.click()

    def open_effect_option_tab(self):
        self._effect_options_tab_button.click()

    def open_mem_timer_tab(self):
        self._mem_timers_tab_button.click()

    def open_active_timer_tab(self):
        self._active_timers_tab_button.click()

    def open_create_timer_tab(self):
        self._create_timer_tab_button.click()

    def expect_submit_request(self):
        return self._page.expect_request(self._SUBMIT_ENDPOINT, timeout=1000)