class Employee:
    def __init__(self, name, ID, salary):
        self.name = name
        self.ID = ID
        self.salary = salary
    
    def travel(self, destination):
        print(f"The Employee is travelling to {destination}")
    

ep1= Employee("Raj", 1, 100000)
ep1.travel("Rajisthan")
