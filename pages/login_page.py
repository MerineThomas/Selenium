from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils import config


class LoginPage(BasePage):
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".oxd-alert-content-text")
    FIELD_ERRORS = (By.CSS_SELECTOR, ".oxd-input-field-error-message")

    def load(self):
        self.open(config.LOGIN_URL)
        return self

    def enter_username(self, username):
        self.type_text(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.type_text(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def attempt_login(self, username, password):
        """Fill in the form and submit. Stays on this page object (use for failed logins)."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        return self

    def login(self, username=config.USERNAME, password=config.PASSWORD):
        """Log in with valid credentials and return the DashboardPage."""
        from pages.dashboard_page import DashboardPage
        self.attempt_login(username, password)
        return DashboardPage(self.driver)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)

    def get_field_errors(self):
        self.find_visible(self.FIELD_ERRORS)
        return [e.text for e in self.find_all(self.FIELD_ERRORS)]

    def is_loaded(self):
        return self.is_displayed(self.LOGIN_BUTTON)
