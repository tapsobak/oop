from dataclasses import dataclass
from typing import List


@dataclass  # we dont need a constructor with the dataclass decorator
class Cars:
    make: str
    model: str
    cost: float
    mileage: int

    def __str__(self):
        return (
            f"Make:    {self.make}\n"
            f"Model:   {self.model}\n"
            f"Cost:    ${self.cost}\n"
            f"Mileage: {self.mileage} miles."
        )


@dataclass
class ElectricCars(Cars):
    range_miles: int

    def __str__(self):
        parent_info = super().__str__()
        return f"{parent_info}\nAutonomy Range: {self.range_miles} miles"


class Concession:
    def __init__(self, name, inventory=None):
        self.name = name
        self.inventory = inventory if inventory is not None else []

    def add_car(self, car):
        self.inventory.append(car)

    def display_car_info(self):
        print(f"***** Welcome to {self.name} *****")
        print("\n--- Inventory ---")
        for car in self.inventory:
            print(f"\n{car}")

    def sell_cars(self, make, model):
        print("\n--- Sales ---")
        for i in range(len(self.inventory)):
            if make == self.inventory[i].make and model == self.inventory[i].model:
                self.inventory.pop(i)
                print(f"\nCar of make: {make} and model: {model} was sold.")
                return

        print(f"\nCar of make: {make} and model: {model} was not found in inventory.")

    def total_cost(self):
        if not self.inventory:
            print("No Cars Available...")
            return
        total_price = 0
        for car in self.inventory:
            total_price += car.cost
        avg_price = total_price / len(self.inventory)
        print("\n--- Price Info ---")
        print(f"Total cost of all cars in the shop: ${total_price}")
        print(f"The average price of a car in the shop: ${avg_price:.2f}")


# Instatiate
camry = Cars("Toyota", "Camry", 35000, 9870)
model3 = ElectricCars("Tesla", "Model 3", 45000, 3300, 450)
fusion = Cars("Ford", "Fusion", 12500, 185000)
c1 = Concession("Concession du Centre")
c1.add_car(camry)
c1.add_car(model3)
c1.add_car(fusion)

if __name__ == "__main__":
    c1.display_car_info()
    c1.sell_cars("Toyota", "Camry")
    c1.total_cost()
