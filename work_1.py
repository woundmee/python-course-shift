#!/usr/bin/python

class Car:

    name = str()
    model = str()
    #speed = int() # 0


    # TODO: что за...

    # def __init__(self): 
    #     self.name = 'unknown'
    #     self.model = 'unknown'
        
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def echo(self):
        print(self.name + ' ' + self.model)


    def start_car(): # завести машину
        print('Машина заведена')
    def stop_car(): # заглушить машину
        print('Машина заглушена')
    def open_hood(): # открыть капот
        print('Копот открыт')
    def close_hood(): # закрыть капот
        print('Копот закрыт')


# автосалон: наследуем класс Car
class CarShowroom(Car):

    # библиотека машин в этом автосалоне
    cars_lst = ['BMW', 'Volvo', 'Toyota']
    models_lst = ['F5', 'CV90', 'Camry']
    

    # TODO: что за...
    def __init__(self):
        Car.name = '_unknown'
        Car.model = '_unknown'

    def __init__(self, name, model):
        Car.name = name
        Car.model =  model

    def get_all_cars(self):
        for c,m in zip(CarShowroom.cars_lst, CarShowroom.models_lst):
            print(f'car: {c}, model: {m}')

    def get_cars(self):
        for car in CarShowroom.cars_lst:
            print('car: ' + car)



# ************ OUT ************** #

cs1 = CarShowroom()
cs1.get_cars()12.02.2024 - 16:00-18:00 по МСК (лекция)  
13.02.2024-16.02.2024 - 09:30-18:00 МСК (09:30-16:00 самостоятельная практика, потом до 18:00 лекция)  
✏️ Измен.: 13.02.2024 обучение будет 10:00-18:30 МСК (09:30-16:30 самостоятельная практика, потом до 18:30 лекция)  
19.02.2024-26.02.2024 - любое удобное время (вам будет выдан доступ в нашу систему СДО, к которой вы сможете подключаться в любое время. В личном кабинете будет материал и видеозаписи для продолжения обучения)





# ************ TEST ************** #

# class Test:

#     car = str()
#     model = str()

#     def __init__(self):
#         self.car = 'unknown'
#         self.model = 'unknown'

#     def __init__(self, name, model):
#         self.car = name
#         self.model = model

#     def echo(self):
#         print(f'name: {self.car}, model: {self.model}')



        
# t = Test()
# t.echo()