from dataclasses import dataclass


@dataclass  # we dont need a constructor with the dataclass decorator
class Car:
    make: str
    model: str
    cost: float
    mileage: int = 0

    def __str__(self):
        return (
            f"Make:    {self.make}\n"
            f"Model:   {self.model}\n"
            f"Cost:    ${self.cost}\n"
            f"Mileage: {self.mileage} miles."
        )


# Instatiate a Car
tesla = Car("Testla", "Model 3", 35000, 9870)

if __name__ == "__main__":
    print(tesla)
