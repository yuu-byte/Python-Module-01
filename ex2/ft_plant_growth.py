class Plant:
    name: str
    height: float
    days_old: int

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.days_old} days old")

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.days_old += 1


if __name__ == "__main__":
    rose = Plant()
    rose.name = "Rose"
    rose.height = 25.0
    rose.days_old = 30

    print("=== Garden Plant Growth ===")
    start_height = rose.height
    rose.show()
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.grow()
        rose.age()
        rose.show()
    total_growth = rose.height - start_height
    print(f"Growth this week: {total_growth:.1f}cm")
