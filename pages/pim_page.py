from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class PIMPage(BasePage):
    HEADER = (By.CSS_SELECTOR, ".oxd-topbar-header-breadcrumb h6")
    ADD_EMPLOYEE_TAB = (By.LINK_TEXT, "Add Employee")
    EMPLOYEE_LIST_TAB = (By.LINK_TEXT, "Employee List")

    # Add Employee form
    FIRST_NAME = (By.NAME, "firstName")
    MIDDLE_NAME = (By.NAME, "middleName")
    LAST_NAME = (By.NAME, "lastName")
    SAVE_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    PERSONAL_DETAILS_HEADING = (By.XPATH, "//h6[normalize-space()='Personal Details']")

    # Employee List search
    EMPLOYEE_NAME_SEARCH = (By.CSS_SELECTOR, "input[placeholder='Type for hints...']")
    SEARCH_BUTTON = (By.XPATH, "//button[normalize-space()='Search']")
    RESULT_ROWS = (By.CSS_SELECTOR, ".oxd-table-body .oxd-table-card")
    NO_RECORDS = (By.XPATH, "//span[normalize-space()='No Records Found']")
    SPINNER = (By.CSS_SELECTOR, ".oxd-form-loader")

    def open_add_employee(self):
        self.click(self.ADD_EMPLOYEE_TAB)
        self.find_visible(self.FIRST_NAME)

    def add_employee(self, first_name, last_name, middle_name=""):
        self.open_add_employee()
        self.type_text(self.FIRST_NAME, first_name)
        if middle_name:
            self.type_text(self.MIDDLE_NAME, middle_name)
        self.type_text(self.LAST_NAME, last_name)
        self.click(self.SAVE_BUTTON)
        self.find_visible(self.PERSONAL_DETAILS_HEADING)

    def is_employee_saved(self):
        return self.is_displayed(self.PERSONAL_DETAILS_HEADING)

    def open_employee_list(self):
        self.click(self.EMPLOYEE_LIST_TAB)
        self.find_visible(self.EMPLOYEE_NAME_SEARCH)

    def search_employee(self, name):
        self.open_employee_list()
        self.type_text(self.EMPLOYEE_NAME_SEARCH, name)
        self.click(self.SEARCH_BUTTON)
        self.wait.until(lambda d: d.find_elements(*self.RESULT_ROWS) or d.find_elements(*self.NO_RECORDS))

    def get_result_count(self):
        return len(self.find_all(self.RESULT_ROWS))

    def get_first_row_text(self):
        return self.find_visible(self.RESULT_ROWS).text
