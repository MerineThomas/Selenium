import time


def test_add_employee(dashboard):
    pim = dashboard.go_to_pim()
    last_name = f"Tester{int(time.time())}"

    pim.add_employee("Auto", last_name)

    assert pim.is_employee_saved()


def test_added_employee_can_be_searched(dashboard):
    pim = dashboard.go_to_pim()
    last_name = f"Finder{int(time.time())}"
    pim.add_employee("Auto", last_name)

    pim.search_employee(last_name)

    assert pim.get_result_count() >= 1
    assert last_name in pim.get_first_row_text()
