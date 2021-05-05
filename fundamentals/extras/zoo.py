class Animal:
    def __init__(self, name, age, health=10, happiness=10):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness
    def display_info(self):
        print(f"name: {self.name}, age: {self.age}, health: {self.health},happiness_level:{self.happiness}")
        return self
    def feed(self):
        self.health += 10
        self.happiness += 10
        return self

class Tiger(Animal):
    def __init__(self, name, age, origin, health = 20, happiness = 15):
        super().__init__(name, age, health, happiness)
        self.origin = origin
    def feed(self):
        if self.health <5:
            self.health += 10
        if self.happiness < 10:
            self.happiness += 10

class Lion(Animal):
    def __init__(self, name, age, health = 15, happiness = 15):
        super().__init__(name, age, health, happiness)
    def feed(self):
        if self.health < 10:
            self.health += 10
        if self.happiness < 10:
            self.happiness += 10

class Bear(Animal):
    def __init__(self, name, age, sex, health = 15, happiness = 10):
        super().__init__(name, age, health, happiness)
        self.sex = sex
    def feed(self):
        if self.health < 10:
            self.health += 10
        if self.happiness < 5:
            self.happiness += 5

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def add_lion(self, name, age):
        self.animals.append( Lion(name, age) )
    def add_tiger(self, name, age, origin):
        self.animals.append( Tiger(name, age, origin) )
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()
            
zoo1 = Zoo("John's Zoo")
zoo1.add_lion("Nala", 10)
zoo1.add_lion("Simba", 5)
zoo1.add_tiger("Rajah", 7 , "China")
zoo1.add_tiger("Shere Khan", 6, "India")
zoo1.print_all_info()