"""Абстрактная фабрика двигателей."""


class Engine:
    """Абстрактный класс топлива."""

    def __init__(self, speed, model, weight, power):
        """Опишем свойства."""
        self.speed = speed
        self.model = model
        self.weight = weight
        self.power = power
        self.cons = 0  # расход топлива

    def fuel_cons(self, distance):
        """Метод подсчета пройденого расхода."""
        return distance * self.cons / 100

    def travel_time(self, distance):
        """Метод подсчета пройденого расстояния."""
        return distance / self.speed


class FromUsa(Engine):
    """Построим двигатель 1."""

    def __init__(self, speed, model, weight, power):
        """Наследуем от класса родителя."""
        super().__init__(speed, model, weight, power)
        self.cons = 5.5  # расход движка


class FromUssr(Engine):
    """Построим двигатель 2."""

    def __init__(self, speed, model, weight, power):
        """Наследуем от класса родителя."""
        super().__init__(speed, model, weight, power)
        self.cons = 28.8
