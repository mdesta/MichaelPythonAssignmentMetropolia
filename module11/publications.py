class Publication:
    def __init__(self, name: str) -> None:
        self.name = name


class Book(Publication):
    def __init__(self, name: str, author: str, page_count: int) -> None:
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self) -> None:
        print(f"Book: {self.name}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.page_count}")


class Magazine(Publication):
    def __init__(self, name: str, chief_editor: str) -> None:
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self) -> None:
        print(f"Magazine: {self.name}")
        print(f"Chief editor: {self.chief_editor}")


def main() -> None:
    donald_duck = Magazine("Donald Duck", "Aki Hyyppä")
    compartment_no_6 = Book("Compartment No. 6", "Rosa Liksom", 192)

    donald_duck.print_information()
    print()
    compartment_no_6.print_information()


if __name__ == "__main__":
    main()
