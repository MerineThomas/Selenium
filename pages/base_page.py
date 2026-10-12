from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    """Generic Selenium wrappers shared by every page object.

    Locators are passed in as tuples, e.g. (By.NAME, "username").
    No assertions here - tests do the asserting.
    """

    DEFAULT_TIMEOUT = 20

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.DEFAULT_TIMEOUT)

    # ---- waiting / finding ----
    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def wait_for_invisible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    # ---- actions ----
    def click(self, locator):
        self.find_clickable(locator).click()

    def type_text(self, locator, text):
        element = self.find_visible(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find_visible(locator).text

    def get_attribute(self, locator, name):
        return self.find(locator).get_attribute(name)

    def is_displayed(self, locator):
        try:
            return self.find_visible(locator).is_displayed()
        except TimeoutException:
            return False

    def hover(self, locator):
        ActionChains(self.driver).move_to_element(self.find_visible(locator)).perform()

    # ---- page-level helpers ----
    def open(self, url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url
