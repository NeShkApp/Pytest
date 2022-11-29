from portmonetka import Wallet
from main_portmonetka import run_command


def test_UserCase():
    wall = Wallet()
    assert run_command(wall, f"add 400\n\radd 500") == False
    assert run_command(wall, "add 400")
    assert wall.info_cash() == 400
    assert run_command(wall, "info")
    assert run_command(wall, "spend 350")
    assert wall.info_cash() == 50
    assert run_command(wall, "spend 200")
    assert wall.info_cash() == 50
    assert run_command(wall, "convert UAH")
