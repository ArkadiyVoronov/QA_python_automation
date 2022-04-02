class Engine:
    def __init__(self, speed, model, weight, power):
        self.speed = speed
        self.model = model
        self.weight = weight
        self.power = power
        self.cons = 0  # расход топлива

    def fuel_cons(self, distance):
        return distance * self.cons / 100

    def travel_time(self, distance):
        return distance / self.speed


class FromUsa(Engine):

    def __init__(self, speed, model, weight, power):
        super().__init__(speed, model, weight, power)
        self.cons = 5.5  # расход движка


class FromUssr(Engine):
    def __init__(self, speed, model, weight, power):
        super().__init__(speed, model, weight, power)
        self.cons = 28.8

#
# engine = FromUsa(25, 'F2', 10, 10)
# distance = 200  # дистанция теста
# print(f'Двигатель FromUsa израсходует {engine.fuel_cons(distance)} литров на {distance} км.')
# print(f'Двигатель FromUsa проедет {distance} км. за {engine.travel_time(distance)}ч.')
#
#
# engine = FromUssr(120, 'B1', 4, 5)
# distance = 200  # дистанция теста
# print(f'Двигатель FromUssr израсходует {engine.fuel_cons(distance)} литров на {distance} км.')
# print(f'Двигатель FromUssr проедет {distance} км. за {engine.travel_time(distance)}ч.')

