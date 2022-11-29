import requests
from portmonetka import Wallet


def currency_conversion(wall: Wallet(), amount, to_currency) -> bool:
    url = "https://api.nbp.pl/api/exchangerates/tables/A/?format=json"
    body = requests.get(url)
    response = body.json()
    k = 0
    # USD, UAH, EUR, CZK
    for rate in response[0]["rates"]:
        if to_currency == rate['code']:
            print(f"You choose {rate['code']}: {rate['currency']}")
            print(f"You have {wall.info_cash()} this currency")
            print(f"Exchange rate of {rate['code']} to PLN: ", rate["mid"])
            result = round(amount * float(rate["mid"]), 2)
            print(f"Your cash in PLN: ", result)
            k += 1
            return True
    if k != 1:
        print("No country with this code founded. Retry with new code.")
        return False
