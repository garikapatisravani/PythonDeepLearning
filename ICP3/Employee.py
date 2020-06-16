class Employee:
    count = 0
    sum = 0
    # Initializing the constructor
    def __init__(self, name, family, salary, department):
        self.emp_department_name = department
        self.emp_salary = salary
        self.emp_family = family
        self.emp_name = name
        Employee.count += 1     # counts the total no of employees
        Employee.sum += self.emp_salary      # sum of salaries of all the employees

    def get_salary(self):   # Method to calculate Average salary of employees
        print(Employee.count)
        return  Employee.sum/Employee.count

# FullTimeEmployee Class inherits the Employee class
class FullTimeEmployee(Employee):
    pass
# Creating the instances for FullTimeEmployee class
f1 = FullTimeEmployee("Sravani", "Garikapati", 120000, "CS")
f2 = FullTimeEmployee("Sums", "Meda", 900000, "CSE")
f3 = FullTimeEmployee("Teja", "Payyavula", 1500000, "CS")
print("Average salary of employess is:", f1.get_salary())