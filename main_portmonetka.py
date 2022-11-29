import re

from portmonetka import Wallet
from currency import currency_conversion


# class InsufficientAmount(Exception):
#     pass

def _print_help():
    print("add <value> - \U0001F4B0 adds money to wallet \U0001F4B0")
    print("spend <value> - \U0001F613 spend money from wallet \U0001F613")
    print("info - \U0001F60E list cash in your wallet \U0001F60E")
    print("convert <country code> - \U0001F60E convert your country cash to PLN \U0001F60E")
    print("quit - \U0001F64B quits the program \U0001F64B")
    print("")


def run_command(wall: Wallet(), cmd: str) -> bool:
    cmd_splits = cmd.split(" ")
    # add
    if cmd_splits[0] == "add":
        if len(cmd_splits) != 2 or cmd_splits[1] == "" or cmd_splits[1] not in re.findall("\d+", cmd_splits[1]):
            print("Invalid input command! Valid form: add <value>")
            return False
        wall.add_cash(int(cmd_splits[1]))
    # spend
    elif cmd_splits[0] == "spend":
        if len(cmd_splits) != 2 or cmd_splits[1] == "" or cmd_splits[1] not in re.findall("\d+", cmd_splits[1]):
            print("Invalid input command! Valid form: spend <value>")
            return False
        wall.spend_cash(int(cmd_splits[1]))
    # info
    elif cmd_splits[0] == "info":
        if len(cmd_splits) != 1:
            print("Invalid input command! Valid form: info")
            return False
        print("Balance: ", wall.info_cash())
    # convert
    elif cmd_splits[0] == "convert":
        if len(cmd_splits) != 2 or cmd_splits[1] == "":
            print("Invalid input command! Valid form: convert <country code> like: UAH, CZK, EUR, USD e.t.c.")
            return False
        currency_conversion(wall, wall.info_cash(), cmd_splits[1])
    else:
        print("Please, input commands from this list:")
        print()
        _print_help()
        return False
    return True


def main():
    print()
    print("Hello, user! That's yours virtual wallet! Have fun!")
    _print_help()
    wallet = Wallet()
    while True:
        cmd = input(">>>")
        if cmd == "quit":
            break
        run_command(wallet, cmd)
    print("Program ended. Bye")


if __name__ == "__main__":
    main()
