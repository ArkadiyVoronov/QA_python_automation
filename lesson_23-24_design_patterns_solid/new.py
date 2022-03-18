# Вы разрабатываете многопользовательскую онлайн игру. Это соревновательный футбольный симулятор.
#
# Актуальная задача реализовать управление командой футболистов. Нужно дать игроку переключаться а нужного
# футболиста, нужно уметь переключать управление на футболиста, который ведет сейчас мяч, нужно придумать
# что делать с теми футболистами которыми игрок сейчас не управляет, чтобы создавалась видимость игры.
#
# Задача - спроектировать систему классами. При выборе определённого шаблона проектирования
# объяснять выбор.

class Command():
    def __init__(self, strategy: Strategy):

    pass




class Player():
    def person(self):
        ...

class Strategy(ABC):
    """Абстрактный метод"""
    @abstractmethod
    def do_algorithm(self, data: List):
        pass


"""
Конкретные Стратегии реализуют алгоритм, следуя базовому интерфейсу Стратегии.
Этот интерфейс делает их взаимозаменяемыми в Контексте.
"""


class ConcreteStrategyA(Strategy):
    """Управление персонажем игроком"""
    def do_algorithm(self, data: List) -> List:
        return sorted(data)


class ConcreteStrategyB(Strategy):
    """Упрадление перснонажем компьютером"""
    def do_algorithm(self, data: List) -> List:
        return reversed(sorted(data))


if __name__ == "__main__":
    # Клиентский код выбирает конкретную стратегию и передаёт её в контекст.
    # Клиент должен знать о различиях между стратегиями, чтобы сделать
    # правильный выбор.

    context = Context(ConcreteStrategyA())
    print("Передаем управление.")
    context.bot()
    print()

    print("Принимаем управление.")
    context.strategy = ConcreteStrategyB()
    context.player()


# from abc import ABC, abstractmethod
# from __future__ import annotations
# 
# 
# class NPC:
#     """Класс игрового персонажа обладающего разным поведением."""
# 
#     _strategy = None
# 
#     def __init__(self, strategy: Strategy) -> None:
#         if not isinstance(strategy, Strategy):
#             raise Exception("Cannot set strategy object")
#         self._strategy = strategy
# 
#     @property
#     def strategy(self) -> Strategy:
#         """проперти, созданное лишь для сеттера."""
#         return self._strategy
# 
#     @strategy.setter
#     def strategy(self, strategy: Strategy) -> None:
#         """Сеттер стратегии."""
#         if not isinstance(strategy, Strategy):
#             raise Exception("Cannot set strategy object")
#         self._strategy = strategy
# 
#     def behave(self) -> None:
#         """Метод игрового поведения персонажа."""
#         print("Игровое поведение персонажа:")
#         print(self._strategy.do_action())
#         print("--Конец исполнения действия--")
# 
# 
# class Strategy(ABC):
#     """Базовый класс стратегии для отнаследования от него."""
# 
#     @abstractmethod
#     def do_action(self):
#         pass
# 
# 
# class AttackStrategy(Strategy):
#     """Класс агрессивного поведения."""
# 
#     def do_action(self) -> str:
#         """Переопределение поведения."""
#         return "Наступает в атаку"
# 
# 
# class RunStrategy(Strategy):
#     """Класс оборонитеьного поведения."""
# 
#     def do_action(self) -> str:
#         """Переопределение поведения."""
#         return "Бежит от страха"
# 
# 
# npc = NPC(AttackStrategy())
# npc.behave()
# npc.strategy = RunStrategy()
# npc.behave()