class Person :
    def __init__(self , name):
        self.name = name

class Teacher(Person) :
    
    def __init__(self , name , subject):
        super().__init__(name)
        self.subject = subject
# Test
t = Teacher("Hassa","Programing")
print(t.name , t.subject)