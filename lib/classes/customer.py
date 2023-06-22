class Customer:
    def __init__(self, name):
        self.name = name

        self._orders = []
        self._coffees = []

    def get_name(self):
        return self._name
    def set_name(self,name):
        if type(name) == str and 1<=len(name)<=15:
            self._name = name
        else:
            raise Exception

    name = property(get_name,set_name)
    



    def orders(self, new_order=None):
        from classes.order import Order

        if isinstance(new_order, Order):
            self._orders.append(new_order)
        return self._orders
    
    def coffees(self, new_coffee=None):
        from classes.coffee import Coffee

        if isinstance(new_coffee,Coffee) and new_coffee not in self._coffees:
            self._coffees.append(new_coffee)
        return self._coffees
        
    def create_order(self,coffee,price):

        from classes.coffee import Coffee
        from classes.order import Order

        if isinstance(coffee,Coffee) and type(price) == int:

            new_Order = Order(self,coffee,price)
            
            #self._orders.append(new_Order)
            #need to add this new_Order to the coffee list order as well as well            call cofee method orders on this. actually this is not necessary since we already did this with the relationships when an order is created. doing it again here is just double counting. 