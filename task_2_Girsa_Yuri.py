class Road:


    def __init__(self, lenght, widght):
        self._lenght = lenght
        self._widht = widght

    def mass_calculator(self, weight=25, thickness=5):
        return f' Масса асфальта: {(self._widht * self._lenght * weight * thickness) // 1000} т'


a = Road(5000, 20)
print(a.mass_calculator())




