"""
student: larissa (2234567)
question 4 - create 2 new classes laptop and tablet (tablet with size, laptop with battery)
"""
from pc import Computer
from portatil import Laptop
from ipad import Tablet

class Computer:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Tablet(Computer):
    def __init__(self, brand, model, size):
        super().__init__(brand, model)
        self.size = size

class Laptop(Computer):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery = battery

my_tablet = Tablet("Apple", "Ipad", "20 inches")
my_laptop = Laptop("Asus", "HyperX", "20.000 mAh")

print(f"My tablet is from brand {my_tablet.brand}, model {my_tablet.model} with size: {my_tablet.size} ")
print(f"My laptop is from brand {my_laptop.brand}, model {my_laptop.model} with battery: {my_laptop.battery}.")

