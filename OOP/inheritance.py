class Animal:
    def __init__ (self, name):
      self.name = name
    
    def eat(self):
       print(f"{self.name} is eating")

    def sleep(self):
       print(f"{self.name} is sleeping")

class Dog(Animal):
   def speak(self):
      print("WOF!")

class Cat(Animal):
   def speak(self):
      print("MEOW!")

dog = Dog("Scooby")
cat = Cat("Tom")

dog.eat()
dog.speak()
cat.sleep()
cat.speak()