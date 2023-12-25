import pytest
from basic_2.bankacc import BankAccount


@pytest.fixture
def account():
    return BankAccount("Udivlun", 1000)


def test_initital_balance(account):
    assert account.get_balance() == 1000


def test_deposit(account):
    account.deposit(50)
    assert account.balance == 1050


def test_withdraw(account):
    account.withdraw(250)
    assert account.balance == 750


def test_insufficient_funds(account):
    with pytest.raises(ValueError, match="The sum 1050 is not allowed"):
        account.withdraw(1050)


def test_multiple_accounts():
    account_1 = BankAccount("Dobryun", 500)
    account_2 = BankAccount("Grustyun", 250)
    account_1.deposit(200)
    account_2.withdraw(150)
    assert account_1.get_balance() == 700
    assert account_2.get_balance() == 100
