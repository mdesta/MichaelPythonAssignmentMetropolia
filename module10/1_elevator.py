class Elevator:
    def __init__(self, bottom_floor: int, top_floor: int) -> None:
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self) -> None:
        if self.current_floor < self.top_floor:
            self.current_floor += 1
        print(f"Elevator at floor {self.current_floor}")

    def floor_down(self) -> None:
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
        print(f"Elevator at floor {self.current_floor}")

    def go_to_floor(self, destination: int) -> None:
        if destination < self.bottom_floor:
            destination = self.bottom_floor
        if destination > self.top_floor:
            destination = self.top_floor

        while self.current_floor < destination:
            self.floor_up()
        while self.current_floor > destination:
            self.floor_down()


def main() -> None:
    elevator = Elevator(1, 10)
    elevator.go_to_floor(5)
    elevator.go_to_floor(1)


if __name__ == "__main__":
    main()
