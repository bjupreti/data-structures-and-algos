from employee import Employee

class FullTimeEmployee(Employee):
    def __init__(self, first_name, last_name, salary):
        super().__init__(first_name, last_name)
        self._salary = salary
        
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, salary):
        self._salary = salary
        
    def get_salary(self):
        return self._salary
    
        