import random


class Car:
    def __init__(self, registration_number: str, maximum_speed: int) -> None:
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.distance = 0.0

    def accelerate(self, change: int) -> None:
        self.current_speed += change
        if self.current_speed < 0:
            self.current_speed = 0
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed

    def drive(self, hours: float) -> None:
        if hours <= 0:
            return
        self.distance += self.current_speed * hours


class Race:
    def __init__(self, name: str, distance_km: int, cars: list[Car]) -> None:
        self.name = name
        self.distance_km = distance_km
        self.cars = cars

    def hour_passes(self) -> None:
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

    def print_status(self) -> None:
        print(f"{self.name} status")
        print(f"{'Car':<10} {'Max':>5} {'Speed':>7} {'Distance':>10}")
        print("-" * 36)
        for car in self.cars:
            print(
                f"{car.registration_number:<10} "
                f"{car.maximum_speed:>5} "
                f"{car.current_speed:>7} "
                f"{car.distance:>10.1f}"
            )
        print()

    def race_finished(self) -> bool:
        return any(car.distance >= self.distance_km for car in self.cars)


def main() -> None:
    cars = [
        Car(f"ABC-{i}", random.randint(100, 200))
        for i in range(1, 11)
    ]

    race = Race("Grand Demolition Derby", 8000, cars)

    hours = 0
    while not race.race_finished():
        race.hour_passes()
        hours += 1
        if hours % 10 == 0:
            race.print_status()

    race.print_status()


if __name__ == "__main__":
    main()
