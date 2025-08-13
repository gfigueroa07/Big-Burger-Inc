# just practicing some classes pweaze dont hate on a latino getting some W motion for his country

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def car_make(self):
        return self.make
    
    def car_model(self):
        return self.model
    
    def car_year(self):
        return self.year
    
    def car_info(self):
        testtest = (f"{self.make} {self.model} {self.year}")
        return testtest

uhh = Car("Toyota", "Corolla", 2099)
ahhh = Car("Honda", "Accord", 1999)

print(uhh.car_info())
print(ahhh.car_model())
        
        
class Xarop:
    def __init__(self, name, age, status):
        self.name = name
        self.age = age
        self.status = status
        
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age

    def get_status(self):
        return self.status

    def get_info(self):
        info = (f"Mr/Mrs. {self.name} is currently {self.age} years old. So this makes {self.name} of {self.status} status")
        return info
Xarop_sensei_UWU = Xarop("Xarop", 50, "unc")        
print(Xarop_sensei_UWU.get_name())
print(Xarop_sensei_UWU.get_age())
print(Xarop_sensei_UWU.get_status())
print(Xarop_sensei_UWU.get_info())