class Plant:
    def __init__(self, name: str, height: float, days_old: int) -> None:
        self._name = name
        if height >= 0:
            self._height = height
        else:
            self._height = 0.0
            print(f"{self._name}: Error, height can't be negative")
        if days_old >= 0:
            self._days_old = days_old
        else:
            self._days_old = 0
            print(f"{self._name}: Error, age can't be negative")

    def set_height(self, height: float) -> None:
        if height >= 0:
            self._height = height
            # print(f"Height updated: {round(self._height, 1)}cm")
        else:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, days_old: int) -> None:
        if days_old >= 0:
            self._days_old = days_old
            # print(f"Age updated: {self._days_old} days")
        else:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._days_old

    def show(self) -> None:
        print(f"{self._name}: "
              f"{round(self._height, 1)}cm, {self._days_old} days old")

    def grow(self, grow_height: float) -> None:
        self.set_height(self._height + grow_height)

    def age(self, past_days: int) -> None:
        self.set_age(self._days_old + past_days)


class Flower(Plant):
    def __init__(self, name: str, height: float,
                 days_old: int, color: str) -> None:
        super().__init__(name, height, days_old)
        self._color = color
        self._is_blooming = False

    def bloom(self) -> None:
        self._is_blooming = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if not self._is_blooming:
            print(f" {self._name} has not bloomed yet")
        else:
            print(f" {self._name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 days_old: int, trunk_diameter: float) -> None:
        super().__init__(name, height, days_old)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade"
              f" of {round(self._height, 1)}cm long"
              f" and {round(self._trunk_diameter, 1)}cm wide.")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {round(self._trunk_diameter, 1)}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float,
                 days_old: int, harvest_season: str) -> None:
        super().__init__(name, height, days_old)
        self._harvest_season = harvest_season
        self._nutritional_value = 0.0

    def grow(self, grow_height: float) -> None:
        super().grow(grow_height)
        self._nutritional_value += grow_height / 42.0

    def age(self, past_days: int) -> None:
        super().age(past_days)
        self._nutritional_value += past_days

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_value:g}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print()

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print()

    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    tomato.grow(42.0)
    tomato.age(20)
    tomato.show()
