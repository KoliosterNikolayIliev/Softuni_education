from project.car import Car


class SportCar(Car):
    DEFAULT_FUEL_CONSUMPTION = 10

    def __init__(self, fuel, horse_power):
        Car.__init__(self, fuel, horse_power)


# sport_car = SportCar(100, 100)
# print(sport_car.fuel)
# sport_car.drive(5)
# print(sport_car.fuel)
