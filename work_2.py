#!/usr/bin/python

# Взять любую тему практики и применить:
#     1. описать вашу предметную область при помощи изученных типов данных
#     2. Обеспечить сериализацию и десериализацию
#     3. Обеспечить валдиацию данных при десериализации

# ========== Автосалон ========== #

import json


# Некая библиотека/справочник машин
class Library:
    cars = [
        {"name": "BMW", "model": "CS F5", "clearance": "10.75", "car_type": "Sport"},
        {"name": "Volvo", "model": "CV90", "clearance": "15.44", "car_type": "Sedan"},
        {"name": "Mazda", "model": "CX-60", "clearance": "12.39", "car_type": "Sedan"},
        {"name": "Toyota", "model": "Camry", "clearance": "14.88", "car_type": "Sedan"}
    ]

    # return all cars in json format
    def get_cars_json(self) -> str:
        jsn = json.dumps(self.cars, ensure_ascii=False, indent=2)
        return jsn


# Класс "Машина" со всеми его параметрами (название машины, модель и тд)
class Car:
    name = str()
    model = str()
    clearance = float()
    car_type = str()

    def __init__(self, name, model, clearance, car_type):
        self.name = name
        self.model = model
        self.clearance = clearance
        self.car_type = car_type

    def get_all_parameter(self):
        car_params = f'NAME={self.name}, MODEL={self.model}, CLEARANCE={self.clearance}, CAR_TYPE={self.car_type}'
        return car_params


# Класс "Автосалон" (...)
# ????? Как здесь применить наследование ?????
class CarShowroom:

    lib = Library()
    car_lib = list()

    data = json.loads(lib.get_cars_json())

    def get_all_cars(self):
        for item in self.data:
            name = str(item["name"])
            model = str(item["model"])
            clearance = float(item["clearance"])
            car_type = str(item["car_type"])

            car = Car(name, model, clearance, car_type)

            print(f'NAME={car.name}\t'
                  f'MODEL={car.model}\t'
                  f'CLEARANCE={car.clearance}\t'
                  f'CAR_TYPE={car.car_type}')


if __name__ == "__main__":
    cs = CarShowroom()
    cs.get_all_cars()
<<<<<<< HEAD


# out:
# описать
=======
>>>>>>> e985c093c424e7144639225457be6f9b4ff02e5f
