from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class DashboardPage(BasePage):
    HEADER = (By.CSS_SELECTOR, ".oxd-topbar-header-breadcrumb h6")
    USER_DROPDOWN = (By.CSS_SELECTOR, ".oxd-userdropdown-tab")
    LOGOUT_LINK = (By.LINK_TEXT, "Logout")
    SPINNER = (By.CSS_SELECTOR, ".oxd-form-loader")

    @staticmethod
    def _menu_item(name):
        return By.XPATH, f"//a[contains(@class,'oxd-main-menu-item')]//span[normalize-space()='{name}']"

    def is_loaded(self):
        return self.is_displayed(self.HEADER)

    def get_header_text(self):
        return self.get_text(self.HEADER)

    def go_to_menu(self, name):
        self.click(self._menu_item(name))

    def go_to_admin(self):
        from pages.admin_page import AdminPage
        self.go_to_menu("Admin")
        return AdminPage(self.driver)

    def go_to_pim(self):
        from pages.pim_page import PIMPage
        self.go_to_menu("PIM")
        return PIMPage(self.driver)

    def logout(self):
        from pages.login_page import LoginPage
        self.click(self.USER_DROPDOWN)
        self.click(self.LOGOUT_LINK)
        return LoginPage(self.driver)
