class Wallet(object):

    def __init__(self, initial_amount=0):
        self.balance = initial_amount

    def spend_cash(self, amount):
        # if amount < 0:
        #     print("You can't spend negative cash)")
        if self.balance < amount:
            print("Not enough available cash to spend: ", amount)
            # raise ValueError
        else:
            self.balance -= amount
            print("Spent cash: ", amount)

    def add_cash(self, amount):
        self.balance += amount
        print("Earned cash: ", amount)


    def info_cash(self):
        return self.balance
