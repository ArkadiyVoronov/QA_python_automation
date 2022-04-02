"""Основной модуль программы."""
from abc import ABC, abstractmethod
from engine.Engine import FromUssr
from fuel_system.Fuel import FromDisel


class RocketBuild(ABC):
    """Абстрактный строитель ракеты."""
    pass


class RocketBuildSpacey(RocketBuild):
    """Построим ракету."""
    def __init__(self):
        self.Engine = Engine
        self.Fuel = Fuel
        pass

