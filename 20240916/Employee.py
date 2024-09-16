class Employee:
    def __init__(self, name, address, code, salary):
        self.name = name
        self.address = address
        self.code = code
        self.salary = salary
    
    def __str__(self):
        return f'{self.name}, {self.address}, {self.code}, {self.salary}'

akhi = Employee("Akhi", '4/123', 'pyul890', 200000)
print(akhi)

