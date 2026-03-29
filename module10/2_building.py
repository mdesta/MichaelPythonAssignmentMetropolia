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


class Building:
    def __init__(self, bottom_floor: int, top_floor: int, elevator_count: int) -> None:
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(elevator_count)]

    def run_elevator(self, elevator_number: int, destination: int) -> None:
        index = elevator_number - 1
        if index < 0 or index >= len(self.elevators):
            print(f"No elevator {elevator_number}")
            return
        self.elevators[index].go_to_floor(destination)


def main() -> None:
    building = Building(1, 10, 3)
    building.run_elevator(1, 5)
    building.run_elevator(2, 10)


if __name__ == "__main__":
    main()
