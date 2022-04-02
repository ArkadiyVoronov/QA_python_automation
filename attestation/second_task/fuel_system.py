"""Абстрактная фабрика топливных отсеков."""
from abc import ABC, abstractmethod


class Fuel(ABC):
    """Абстрактный класс топлива."""

    def __init__(self, volume, model, weight, type_f):
        """Опишем свойства."""
        self.volume = volume
        self.model = model
        self.weight = weight
        self.type = type_f
        self.cons = 0  # расход топлива

    def fuel_cons(self, distance):
        """Метод подсчета пройденого расхода."""
        return distance * self.cons / 100

    def travel_time(self, distance):
        """Метод подсчета пройденого расстояния."""
        return distance / self.volume


class FromDisel(Fuel):
    """Построим топливную систему 1."""

    def __init__(self, volume, model, weight, type_f):
        """Наследуем от класса родителя."""
        super().__init__(volume, model, weight, type_f)
        self.cons = 5.5  # расход движка


class FromPetrol(Fuel):
    """Построим топливную систему 2."""

    def __init__(self, volume, model, weight, type_f):
        """Наследуем от класса родителя."""
        super().__init__(volume, model, weight, type_f)
        self.cons = 28.8
