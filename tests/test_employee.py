import pytest
from Employee import employee

def test_imported_employee():
#    t_employee = employee("Pandych", "sleepper", 2000)
    main_employee = employee.employee1

    assert main_employee.name == 'Doveryun'
    assert main_employee.position == 'QA'
    assert main_employee.salary == 3000

