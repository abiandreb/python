class Store:
    total_sells = 0

    def __init__(self, name, sell_amount):
        self._name = name
        self._sell_amount = sell_amount
        Store.total_sells += sell_amount

    def get_sell_amount(self):
        return self._sell_amount

    def set_sell_amount(self, amount):
        self._sell_amount = amount
        Store.total_sells += amount

    def get_name(self):
        return self._name


atb = Store('ATB', 200)
silpo = Store('Silpo', 300)
larok = Store('Larok', 10)

# Print total sells
print(Store.total_sells)

# Set new sells value
atb.set_sell_amount(3000)

# Print new total sells value
print(Store.total_sells)

