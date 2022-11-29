from portmonetka import Wallet
from main_portmonetka import run_command
from currency import currency_conversion


def test_run_add():
    wall = Wallet()
    assert run_command(wall, "add 300")
    assert wall.info_cash() == 300
    assert run_command(wall, "add 200")
    assert wall.info_cash() == 500


def test_run_add_bad_argument():
    wall = Wallet()
    assert run_command(wall, "add 13 1") == False
    assert wall.info_cash() == 0
    assert run_command(wall, "add ") == False
    assert wall.info_cash() == 0


def test_run_spend():
    wall = Wallet(20)
    assert run_command(wall, "spend 10")
    assert wall.info_cash() == 10
    assert run_command(wall, "spend 1")
    assert wall.info_cash() == 9

def test_run_spend_bad_argument():
    wall = Wallet(20)
    assert run_command(wall, "spend 100")
    assert wall.info_cash() == 20
    assert run_command(wall, "spend 1 10") == False
    assert wall.info_cash() == 20
    assert run_command(wall, "spend -33jfdfk") == False
    assert wall.info_cash() == 20


def test_info():
    wall = Wallet(46)
    assert wall.info_cash() == 46


def test_run_currency():
    wallet = Wallet(200)
    assert currency_conversion(wallet, wallet.info_cash(), "CZK")

def test_run_bad_currency():
    wallet = Wallet(200)
    assert currency_conversion(wallet, wallet.info_cash(), "fsgdfgfd1") == False






