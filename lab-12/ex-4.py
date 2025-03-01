class Employee:
    company = "TechCorp"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


e1 = Employee("Alice", 50000)
e2 = Employee("Bob", 60000)

print(e1.company)
print(e2.company)

Employee.company = "NewTechCorp"

print(e1.company)
print(e2.company)
