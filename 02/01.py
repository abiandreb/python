class Vehicle:

    def __init__(self, brand, color, vehicle_class='Car'):
        self._brand = brand
        self._color = color
        self._max_passengers = 4
        self._wheels = 4
        self._vehicle_class = vehicle_class

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    def max_pass_passengers(self):
        return self._max_passengers

    def wheels(self):
        return self._wheels

    def __str__(self):
        return f'Brand: {self._brand}, color: {self._color}'


class Truck(Vehicle):

    def max_pass_passengers(self):
        return 2

    def wheels(self):
        return 8


class Bus(Vehicle):

    def max_pass_passengers(self):
        return 25

    def wheels(self):
        return 6
