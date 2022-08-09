import csv

class Item:
    """
    Item class
    """
    # class attributes
    pay_rate = 0.8 # The pay rate after 20% discount.
    all = []
    
    def __init__(self, name: str, price: float, quantity=0):
        print(f"An instance created: {name}")
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!!"
        
        # Assign to self object (instance attributes)
        self.__name = name
        self.__price = price
        self.quantity = quantity
        
        # Actions to execute
        Item.all.append(self)
        
    @property
    # Property Decorator = Read-only attribute
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if len(value) >= 10:
            raise Exception("The name is too long!")
        self.__name = value
        
    @property
    def price(self):
        return self.__price
    
    def apply_discount(self):
        self.__price = self.__price * self.pay_rate
        
    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value
        
    def calculate_total_price(self):
        return self.__price * self.quantity
    
        
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name=item['name'],
                price=float(item['price']),
                quantity=int(item['quantity'])
            )
    
    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
        
        
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"
    
    def __connect(self, smtp_server):
        pass
    
    def __prepare_body(self):
        return f"""
        Hello someone.
        We have {self.name} {self.quantity} times.
        """
    
    def __send(self):
        pass
    
    def send_email(self):
        """
        Example of abstraction. 
        Abstracting the information that is unnecessary to the callee.
        """
        self.__connect('')
        self.__prepare_body()
        self.__send()
    