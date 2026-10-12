import pytest


@pytest.mark.smoke
def test_logout_returns_to_login_page(dashboard):
    login_page = dashboard.logout()

    assert login_page.is_loaded()
    assert "login" in login_page.get_current_url()


def test_dashboard_title(dashboard):
    assert dashboard.get_title() == "OrangeHRM"
