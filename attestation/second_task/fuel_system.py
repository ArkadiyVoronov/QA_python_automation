class Fuel:
    def __init__(self, volume, model, weight, type):
        self.volume = volume
        self.model = model
        self.weight = weight
        self.type = type
        self.cons = 0  # расход топлива

    def fuel_cons(self, distance):
        return distance * self.cons / 100

    def travel_time(self, distance):
        return distance / self.volume


class FromDisel(Fuel):

    def __init__(self, volume, model, weight, type):
        super().__init__(volume, model, weight, type)
        self.cons = 5.5  # расход движка


class FromPetrol(Fuel):
    def __init__(self, volume, model, weight, type):
        super().__init__(volume, model, weight, type)
        self.cons = 28.8


# engine = FromDisel(25, 'T1000', 10, 'disel')
# distance = 200  # дистанция теста
# print(f'Двигатель FromDisel израсходует {engine.fuel_cons(distance)} литров на {distance} км.')
# print(f'Двигатель FromDisel проедет {distance} км. за {engine.travel_time(distance)}ч.')
#
#
# engine = FromPetrol(120, 'X1', 4, 'petrol')
# distance = 200  # дистанция теста
# print(f'Двигатель FromPetrol израсходует {engine.fuel_cons(distance)} литров на {distance} км.')
# print(f'Двигатель FromPetrol проедет {distance} км. за {engine.travel_time(distance)}ч.')