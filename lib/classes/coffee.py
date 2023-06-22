class Coffee:
    def __init__(self, name):
        if type(name) == str:
            self.name = name
        else:
            raise Exception
        self._orders = []
        self._customers = []

    def get_name(self):
        return self._name
    
    def set_name(self,name):
        if type(name)==str and not hasattr(self,'name'):
            self._name=name
        else:
            raise Exception

    name = property(get_name,set_name)
        
    def orders(self, new_order=None): #return a list of all orders that has this coffee instance
        from classes.order import Order
        
        if isinstance(new_order,Order):
            self._orders.append(new_order)
        return self._orders
    
    def customers(self, new_customer=None): #returns a list of all customers that has this cofee instance
        from classes.customer import Customer
        
        if isinstance(new_customer,Customer) and new_customer not in self._customers:
            self._customers.append(new_customer)
        return self._customers
    
    def num_orders(self):
        return len(self._orders)
    
    def average_price(self): #cofee in general and not a specific cofee is how i read it.
        total = 0
        for item in self._orders:
            total += item.price
        return (total/len(self._orders))