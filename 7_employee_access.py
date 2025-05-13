class Employee:
    
    def __init__(self, name , salary , ssn ):
        self.name = name          # Public attribute
        self._salary = salary     # Protected attribute (by convention)
        self.__ssn = ssn          # Private attribute (name mangled)

# Test
emp = Employee("Hassan",50000 ,"123-45-6789")

print(emp.name)            # Public: directly accessible
print(emp._salary)         # Protected: accessible but not recommended
# print(emp.__ssn)         # Error: private attribute, not directly accessible
print(emp._Employee__ssn)  # Accessing private attribute using name mangling