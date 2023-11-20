class Coffee:

    all = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        if isinstance(name, str):
            if hasattr(self, "_name") == False and len(name) > 2:
                self._name = name

    def __init__(self, name):
        self.name = name
        Coffee.all.append(self)
        
    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        return(list(set([order.customer for order in Order.all if order.coffee == self])))
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        prices = [order.price for order in self.orders()]
        if len(prices) > 0:
            return sum(prices) / len(prices)
        else:
            return 0

class Customer:

    all = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        if isinstance(name, str):
            if len(name) > 0 and len(name) < 16:
                self._name = name

    def __init__(self, name):
        self.name = name
        Customer.all.append(self)
        
    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        return list(set([order.coffee for order in Order.all if order.customer == self]))
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
    @classmethod
    def most_aficionado(cls, coffee):
        leading_customer = None
        most_spent = 0
        for customer in cls.all:
            amount_spent = 0
            relevant_orders = [order for order in customer.orders()]
            if coffee in [order.coffee for order in relevant_orders]:
                amount_spent = sum([order.price for order in relevant_orders])
                if amount_spent > most_spent:
                    leading_customer = customer
                    most_spent = amount_spent
        return leading_customer
    
class Order:

    all = []

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if isinstance(price, float):
            if price >= 1 and price <= 10 and hasattr(self, "_price") == False:
                self._price = price


    def __init__(self, customer, coffee, price):
        if customer in Customer.all and coffee in Coffee.all:
            self.customer = customer
            self.coffee = coffee
            self.price = price
            Order.all.append(self)