class Dog :
    
    def __init__(self , name , bread ):
        self.name = name
        self.bread = bread
        
    def bark(self):
        print(f"{self.name}Is Says Woof!")
        
# Test
d = Dog("Rex", "German Shepherd")
d.bark()