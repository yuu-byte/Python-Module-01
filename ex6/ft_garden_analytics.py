class Plant:
    class Statistics:
        def __init__(self) -> None:
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

        def record_grow(self) -> None:
            self._grow_count += 1

        def record_age(self) -> None:
            self._age_count += 1

        def record_show(self) -> None:
            self._show_count += 1

        def show_stats(self) -> None:
            print(f" Stats: {self._grow_count} grow, "
                  f"{self._age_count} age, {self._show_count} show")

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
        self._stats = Plant.Statistics()

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
        self._stats.record_show()

    def grow(self, grow_height: float) -> None:
        self.set_height(self._height + grow_height)
        self._stats.record_grow()

    def age(self, past_days: int) -> None:
        self.set_age(self._days_old + past_days)
        self._stats.record_age()

    def show_stats(self) -> None:
        self._stats.show_stats()

    @staticmethod
    def is_over_year(days: int) -> bool:
        return days > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)


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


class Seed(Flower):
    def __init__(self, name: str, height: float,
                 days_old: int, color: str) -> None:
        super().__init__(name, height, days_old, color)
        self._seed_count = 0

    def bloom(self) -> None:
        super().bloom()
        self._seed_count = 42

    def show(self) -> None:
        super().show()
        print(f" Seeds {self._seed_count}")


class Tree(Plant):
    class TreeStatistics(Plant.Statistics):
        def __init__(self) -> None:
            super().__init__()
            self._produce_shade_count = 0

        def record_produce_shade(self) -> None:
            self._produce_shade_count += 1

        def show_stats(self) -> None:
            super().show_stats()
            print(f" {self._produce_shade_count} shade")

    _stats: TreeStatistics

    def __init__(self, name: str, height: float,
                 days_old: int, trunk_diameter: float) -> None:
        super().__init__(name, height, days_old)
        self._trunk_diameter = trunk_diameter
        self._stats = Tree.TreeStatistics()

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade"
              f" of {round(self._height, 1)}cm long"
              f" and {round(self._trunk_diameter, 1)}cm wide.")
        self._stats.record_produce_shade()

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


def display_statistics(plant: Plant) -> None:
    plant.show_stats()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_over_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_over_year(400)}")
    print()

    print("===Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[statistics for Rose]")
    rose.show_stats()
    print("[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.bloom()
    rose.show()
    print("[statistics for Rose]")
    rose.show_stats()
    print()

    print("===Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[statistics for Oak]")
    oak.show_stats()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    oak.show_stats()
    print()

    print("===Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    print("[statistics for Sunflower]")
    sunflower.show_stats()
    print()

    print("===Anonymous")
    unknown = Plant.create_anonymous()
    unknown.show()
    print("[statistics for Unknown plant]")
    unknown.show_stats()
