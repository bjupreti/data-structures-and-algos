class Payroll:
    def __init__(self):
        self._employee_list = []
        
    @property
    def employee_list(self):
        return self._employee_list
    
    @employee_list.setter
    def employee_list(self, list):
        self._employee_list = list
        
        
    def add_employee(self, employee):
        self._employee_list.append(employee)
        
    def print(self):
        for employee in self._employee_list:
            print(f"{employee.full_name} \t ${employee.get_salary()}")