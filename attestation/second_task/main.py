"""Основной модуль программы."""
from engine.Engine import FromUssr
from fuel_system.Fuel import FromDisel


def rocket():
    """Строим ракету."""
    FromDisel(25, 'T1000', 10, 'disel')
    FromUssr(120, 'B1', 4, 5)


print(rocket())
