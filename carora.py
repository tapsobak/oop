from dataclasses import dataclass


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


# Instatiate
camry = Cars("Toyota", "Camry", 35000, 9870)
model3 = ElectricCars("Tesla", "Model 3", 45000, 3300, 450)


if __name__ == "__main__":
    print("--- Gas Car ---")
    print(camry)
    print("\n--- Electric Car ---")
    print(model3)
