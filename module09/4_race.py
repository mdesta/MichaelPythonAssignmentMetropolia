import random


class Car:
    def __init__(self, registration_number: str, maximum_speed: int) -> None:
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0.0

    def accelerate(self, change: int) -> None:
        self.current_speed += change
        if self.current_speed < 0:
            self.current_speed = 0
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed

    def drive(self, hours: float) -> None:
        if hours <= 0:
            return
        self.travelled_distance += self.current_speed * hours


def print_car_table(cars: list[Car]) -> None:
    print(f"{'Car':<10} {'Max':>5} {'Speed':>7} {'Distance':>10}")
    print("-" * 36)
    for car in cars:
        print(
            f"{car.registration_number:<10} "
            f"{car.maximum_speed:>5} "
            f"{car.current_speed:>7} "
            f"{car.travelled_distance:>10.1f}"
        )


def main() -> None:
    cars = [
        Car(f"ABC-{i}", random.randint(100, 200))
        for i in range(1, 11)
    ]

    while True:
        for car in cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

        if any(car.travelled_distance >= 10_000 for car in cars):
            break

    print("Race results")
    print_car_table(cars)


if __name__ == "__main__":
    main()
