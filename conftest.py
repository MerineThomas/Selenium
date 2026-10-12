import os
from datetime import datetime

import pytest
from selenium import webdriver

from pages.login_page import LoginPage


def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", help="Run Chrome without a visible window")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Keep the test result on the item so the driver fixture can see if it failed."""
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)


@pytest.fixture
def driver(request):
    options = webdriver.ChromeOptions()
    if request.config.getoption("--headless"):
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    browser = webdriver.Chrome(options=options)
    if not request.config.getoption("--headless"):
        browser.maximize_window()

    yield browser

    # Screenshot when a test fails
    report = getattr(request.node, "rep_call", None)
    if report is not None and report.failed:
        os.makedirs("screenshots", exist_ok=True)
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        browser.save_screenshot(f"screenshots/{request.node.name}_{stamp}.png")
    browser.quit()


@pytest.fixture
def login_page(driver):
    return LoginPage(driver).load()


@pytest.fixture
def dashboard(login_page):
    """A browser already logged in with valid credentials, sitting on the dashboard."""
    dashboard_page = login_page.login()
    assert dashboard_page.is_loaded(), "Dashboard did not load after login"
    return dashboard_page
