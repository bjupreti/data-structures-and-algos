from full_time_employee import FullTimeEmployee
from hourly_employee import HourlyEmployee
from payroll import Payroll

payroll = Payroll()

payroll.add_employee(FullTimeEmployee('Bijay', 'Upreti', 1000))
payroll.add_employee(FullTimeEmployee('Bishal', 'Sapkota', 2000))
payroll.add_employee(HourlyEmployee('Nikesh', 'Sapkota', 100, 30))

payroll.print()