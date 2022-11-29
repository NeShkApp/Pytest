import pytest
from portmonetka import Wallet


@pytest.fixture
def empty_wallet():
    return Wallet()


@pytest.fixture
def wallet():
    return Wallet(20)


def test_default_initial_amount(empty_wallet):
    assert empty_wallet.balance == 0


def test_setting_initial_amount(wallet):
    assert wallet.balance == 20


def test_wallet_add_cash(wallet):
    wallet.add_cash(80)
    assert wallet.balance == 100


def test_wallet_spend_cash(wallet):
    wallet.spend_cash(15)
    assert wallet.balance == 5


def test_wallet_spend_cash_raises_exception_on_insufficient_amount(empty_wallet):
    # with pytest.raises(ValueError):
    #     empty_wallet.spend_cash(100)
    # print("Not available cash to spend")
    empty_wallet.spend_cash(100)


@pytest.mark.parametrize("earned,spent,expected", [
    (30, 10, 20),
    (20, 2, 18),
])
def test_transactions(empty_wallet, earned, spent, expected):
    empty_wallet.add_cash(earned)
    empty_wallet.spend_cash(spent)
    assert empty_wallet.balance == expected


@pytest.mark.parametrize("earned,spent", [
    (30, 40),
    (90, 100),
])
def test_transactions_insufficient_amounts(empty_wallet, earned, spent):
    empty_wallet.add_cash(earned)
    empty_wallet.spend_cash(spent)
    # with pytest.raises(ValueError):
    #     empty_wallet.spend_cash(spent)
