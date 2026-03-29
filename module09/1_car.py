class Car:
    def __init__(self, registration_number: str, maximum_speed: int) -> None:
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0.0


def main() -> None:
    car = Car("ABC-123", 142)

    print("Initial car properties")
    print(f"Registration: {car.registration_number}")
    print(f"Max speed: {car.maximum_speed} km/h")
    print(f"Current speed: {car.current_speed} km/h")
    print(f"Travelled distance: {car.travelled_distance:.1f} km")


if __name__ == "__main__":
    main()
