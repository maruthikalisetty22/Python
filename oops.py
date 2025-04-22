class Dog():
    #Class object attriburte
    species = "Mammal"
    
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def display(self):
        print(f"{self.name} is barking woof!!! and its breed is {self.breed} and its species is {Dog.species}") #We can call class object var or attr as Class.attribute or self.attribute {self.species}
        

dog_object = Dog(name = "Julie", breed = "Daburman")

print(type(dog_object))
print(dog_object.name)
print(dog_object.breed)
print(dog_object.species)
dog_object.display()
