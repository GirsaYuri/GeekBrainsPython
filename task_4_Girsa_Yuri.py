import random


class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала!'

    def stop(self):
        return f'{self.name} остановилась!'

    def turn(self):
        direction = ['влево', 'вправо']
        turn = random.choice(direction)
        return f'{self.name} повернула {turn}'

    def show_speed(self):
        return f'{self.name} скорость {self.speed}'


class TownCar(Car):

    def show_speed(self):
        return f'{self.name} скорость автомобиля {self.speed}. Превышение скорости!' \
            if self.speed > 60 else f'{self.name}: скорость автомобиля: {self.speed}'


class WorkCar(Car):
    'какая то машина '


class PoliceCar(Car):

    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


police_car = PoliceCar(90, 'белая', 'Audi')
print(police_car.go())

car_1 = Car(20, 'green', "Mc'Queen")
print(car_1.go())
print(car_1.turn())
print(car_1.stop())
