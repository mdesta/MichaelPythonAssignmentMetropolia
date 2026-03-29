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


def main() -> None:
    car = Car("ABC-123", 142)

    car.current_speed = 60
    car.travelled_distance = 2000
    car.drive(1.5)

    print(f"Distance after driving 1.5h at 60 km/h: {car.travelled_distance:.1f} km")


if __name__ == "__main__":
    main()
