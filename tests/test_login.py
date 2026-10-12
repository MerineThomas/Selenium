import pytest

from utils import config


@pytest.mark.smoke
def test_valid_login_lands_on_dashboard(login_page):
    dashboard = login_page.login(config.USERNAME, config.PASSWORD)

    assert dashboard.is_loaded()
    assert dashboard.get_header_text() == "Dashboard"
    assert "dashboard" in dashboard.get_current_url()


def test_invalid_login_shows_error(login_page):
    login_page.attempt_login("WrongUser", "wrong-password")

    assert login_page.get_error_message() == "Invalid credentials"


def test_empty_fields_show_required_errors(login_page):
    login_page.click_login()

    assert login_page.get_field_errors() == ["Required", "Required"]


@pytest.mark.parametrize(
    "username, password",
    [
        ("Admin", "wrong"),
        ("wrong", "admin123"),
        ("ADMIN_X", "admin"),
    ],
)
def test_bad_credential_combinations(login_page, username, password):
    login_page.attempt_login(username, password)

    assert login_page.get_error_message() == "Invalid credentials"
