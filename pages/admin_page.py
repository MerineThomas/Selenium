from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AdminPage(BasePage):
    HEADER = (By.CSS_SELECTOR, ".oxd-topbar-header-breadcrumb h6")
    USERNAME_INPUT = (
        By.XPATH,
        "//label[normalize-space()='Username']/ancestor::div[contains(@class,'oxd-input-group')]//input",
    )
    SEARCH_BUTTON = (By.XPATH, "//button[normalize-space()='Search']")
    RESULT_ROWS = (By.CSS_SELECTOR, ".oxd-table-body .oxd-table-card")
    RECORDS_FOUND = (By.XPATH, "//span[contains(.,'Record') and contains(.,'Found')]")
    NO_RECORDS = (By.XPATH, "//span[normalize-space()='No Records Found']")
    SPINNER = (By.CSS_SELECTOR, ".oxd-form-loader")

    def is_loaded(self):
        return "admin" in self.get_current_url().lower() and self.is_displayed(self.USERNAME_INPUT)

    def search_user(self, username):
        self.type_text(self.USERNAME_INPUT, username)
        self.click(self.SEARCH_BUTTON)
        self.wait_for_invisible(self.SPINNER)
        self.wait.until(lambda d: d.find_elements(*self.RESULT_ROWS) or d.find_elements(*self.NO_RECORDS))

    def get_result_count(self):
        return len(self.find_all(self.RESULT_ROWS))

    def get_first_row_text(self):
        return self.find_visible(self.RESULT_ROWS).text

    def get_records_found_text(self):
        return self.get_text(self.RECORDS_FOUND)

    def is_no_records_shown(self):
        return self.is_displayed(self.NO_RECORDS)
