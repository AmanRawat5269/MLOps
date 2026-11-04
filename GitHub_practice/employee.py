class Employee:
    def __init__(self, Name, Employee_id, salary):
        self.name = Name
        self.employee_id = Employee_id
        self.salary = salary
        
    
    def display_details(self):
        print(f"Name of the employee is : {self.name}")
        print(f"Employee ID is : {self.employee_id}")
        print(f"Salary of the employee is : {self.salary}")
        
    def give_raise(self, amount):
        self.salary += amount
        print(f"Updated salary: {self.salary}")


emp1 = Employee('Aman', 10, 1200000)
emp1.display_details()
emp1.give_raise(50000)