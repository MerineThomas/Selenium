def test_navigate_to_admin(dashboard):
    admin = dashboard.go_to_admin()

    assert admin.is_loaded()


def test_search_existing_user(dashboard):
    admin = dashboard.go_to_admin()
    admin.search_user("Admin")

    assert admin.get_result_count() >= 1
    assert "Admin" in admin.get_first_row_text()


def test_search_unknown_user_shows_no_records(dashboard):
    admin = dashboard.go_to_admin()
    admin.search_user("zzz_no_such_user_zzz")

    assert admin.is_no_records_shown()
