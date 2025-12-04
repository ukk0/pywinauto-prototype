from pywinauto import Application, Desktop


class LogCollector:
    def __init__(self, exe_path: str, app_title_re: str):
        self.exe_path = exe_path
        self.app_title = app_title_re
        self.app = Application(backend="uia").start(self.exe_path)
        self.dlg = Desktop(backend="uia").window(title_re=self.app_title)

        self.profile_dropdown = self.dlg.child_window(
            title="Collection profile", control_type="ComboBox"
        )
        self.collect_button = self.dlg.child_window(
            title="Collect", control_type="Button"
        )
        self.close_button = self.dlg.child_window(title="Close", control_type="Button")
        self.ok_button = self.dlg.child_window(title="OK", control_type="Button")

    def print_app_locators(self):
        self.dlg.print_control_identifiers()

    def select_collection_profile(self, profile: str):
        self.profile_dropdown.select(profile)

    def toggle_checkbox_on(self, checkbox_label: str):
        toggle = self.dlg.child_window(
            title=checkbox_label, control_type="ListItem"
        ).wrapper_object()
        toggle.click_input()
        toggle.type_keys("{SPACE}")

    def start_collection(self):
        self.collect_button.click()

    def close_confirmation_popup(self):
        self.ok_button.wait(wait_for="enabled", timeout=5)
        self.ok_button.click()

    def close_application(self):
        self.close_button.click()
