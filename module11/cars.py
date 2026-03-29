class Car:
    def __init__(self, registration_number: str, maximum_speed: float) -> None:
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0.0
        self.kilometers = 0.0

    def set_speed(self, speed: float) -> None:
        if speed < 0:
            speed = 0
        if speed > self.maximum_speed:
            speed = self.maximum_speed
        self.current_speed = speed

    def drive(self, hours: float) -> None:
        if hours < 0:
            return
        self.kilometers += self.current_speed * hours


class ElectricCar(Car):
    def __init__(self, registration_number: str, maximum_speed: float, battery_capacity_kwh: float) -> None:
        super().__init__(registration_number, maximum_speed)
        self.battery_capacity_kwh = battery_capacity_kwh


class GasolineCar(Car):
    def __init__(self, registration_number: str, maximum_speed: float, tank_volume_l: float) -> None:
        super().__init__(registration_number, maximum_speed)
        self.tank_volume_l = tank_volume_l


def main() -> None:
    electric = ElectricCar("ABC-15", 180, 52.5)
    gasoline = GasolineCar("ACD-123", 165, 32.3)

    electric.set_speed(120)
    gasoline.set_speed(95)

    electric.drive(3)
    gasoline.drive(3)

    print(f"{electric.registration_number} distance: {electric.kilometers:.1f} km")
    print(f"{gasoline.registration_number} distance: {gasoline.kilometers:.1f} km")


if __name__ == "__main__":
    main()
