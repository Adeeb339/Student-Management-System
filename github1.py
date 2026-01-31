class car:
    brand=""
    model=""
    color=""
    def __init__(self,br,m,c):
        self.brand=br
        self.model=m
        self.color=c
    def show_details(self):
        print(f"Brand: {self.brand} | Model: {self.model} | color: {self.color}")

class electric_car(car):
    battery=""
    fuel_type=""
    battery_life=""
    def __init__(self, br, b, m, c, bl, f):
        self.battery=br
        self.fuel_type=f
        self.battery_life=bl
        self.brand=b
        self.model=m

car1=car("Toyota", "Corrola", "White")


car1.show_details()
print("Hello")