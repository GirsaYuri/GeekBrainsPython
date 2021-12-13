import time
class TrafficLight:


    def running(self):
        self.__color = 'Красный сигнал светофора'
        print(f'{self.__color}')
        time.sleep(7)
        self.__color = 'Желтый сигнал светофора'
        print(f'{self.__color}')
        time.sleep(2)
        self.__color = 'Зеленый сигнал светофора'
        print(f'{self.__color}')
        time.sleep(5)

a = TrafficLight()
a.running()




