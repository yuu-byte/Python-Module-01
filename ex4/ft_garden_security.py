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
            print(f"Height updated: {round(self._height, 1)}cm")
        else:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, days_old: int) -> None:
        if days_old >= 0:
            self._days_old = days_old
            print(f"Age updated: {self._days_old} days")
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

    def grow(self) -> None:
        self._height += 0.8

    def age(self) -> None:
        self._days_old += 1


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    print("Plant created: ", end="")
    rose.show()
    print("")

    rose.set_height(25.0)
    rose.set_age(30)
    print("")

    rose.set_height(-42.0)
    rose.set_age(-42)
    print("")

    print("Current state: ", end="")
    rose.show()
