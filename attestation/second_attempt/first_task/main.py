"""Прототип системы, которая смотрит за курьерами."""

from abc import ABC, abstractmethod


class System(ABC):
    """Интерфейс общий для всей системы."""
    @abstractmethod
    def get_curier_on_map(self):
        pass


class AggregatorMediator(ABC):
    """Создаем посредника, согласно соответствующему шаблону."""
    @abstractmethod
    def get_curier_online(self):
        pass

    @abstractmethod
    def get_curier_on_task(self):
        pass


class Aggregator(AggregatorMediator):
    """Реализация конкретной логики взаимодействия."""
    def get_curier_online(self):
        print("узнать у устройства онлайн ли оно")

    def get_curier_on_task(self):
        print("выполняет ли курьер доставку прямо сейчас")


class Map():
    """Карта для отрисовки клиентов."""
    def get_curier_on_map(self):
        print("Получаем всех курьеров на карте")
