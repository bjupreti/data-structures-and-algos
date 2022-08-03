import requests

class Employee:
    """A sample Employee class"""
    # class attributes
    raise_amount = 1.05
    
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        
    @property
    def email(self):
        return f"{self.fname}.{self.lname}@email.com"
    
    @property
    def fullname(self):
        return f"{self.fname} {self.lname}"
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        
    def monthly_schedule(self, month):
        response = requests.get(f"http://company.com/{self.lname}/{month}")
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'