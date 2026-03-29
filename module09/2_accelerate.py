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


def main() -> None:
    car = Car("ABC-123", 142)

    car.accelerate(30)
    car.accelerate(70)
    car.accelerate(50)
    print(f"Speed after accelerations: {car.current_speed} km/h")

    car.accelerate(-200)
    print(f"Speed after emergency brake: {car.current_speed} km/h")


if __name__ == "__main__":
    main()
