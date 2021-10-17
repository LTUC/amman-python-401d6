class SomeClass:
    def __init__(self, price=0):
        # underscore means that we do not want code outside of your class to touch these values
        self._price
        self._shelf

    def get_price(self):
        return self._price * 1.10

    def get_shelf(self):
        return self._shelf


item = SomeClass(20)

item.get_price()
