
class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)
    #relationships
        self.coffee.orders(self) #Add this order to the coffee
        self.coffee.customers(self.customer) #add this customer to the coffee
        
        self.customer.orders(self) #Add this order to the customer
        self.customer.coffees(self.coffee) #add this cofee to the customer


    def get_price(self):
        return self._price
    def set_price(self,price):
        if 1<=price<=10:
            self._price = price
        else:
            raise Exception

    price = property(get_price,set_price)

    def get_customer(self):
        return self._customer
    
    def set_customer(self,customer): #Customer class
        from classes.customer import Customer
        if isinstance(customer,Customer):
            self._customer = customer
        else:
            raise Exception

    customer = property(get_customer,set_customer)

    def get_coffee(self):
        return self._coffee
    
    def set_coffee(self,coffee):
        from classes.coffee import Coffee
        if isinstance(coffee,Coffee):
            self._coffee = coffee
        else:
            raise Exception
        
    coffee = property(get_coffee,set_coffee)