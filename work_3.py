#!/usr/bin/python

# Задачи практики
# Подготовить HTML/XML-документ с данными ранее выбранной предметной области (автосалон)
# С помощью библиотеки BeautifulSoup разобрать HTML/XML-документ
# Валидировать его содержимое одним из способов (важное)

# ==== START ==== #
from bs4 import BeautifulSoup
# from pydantic import BaseModel, validator


# Some Xml container/class
class Xml:
    xml = """
    <?xml version="1.0" encoding="UTF-8"?>
    <CarShowroom>
        <Car>
            <name>BMW</name>
            <model>F5 CS</model>
            <clearance>10.58</clearance>
        </Car>
        <Car>
            <name>Toyota</name>
            <model>Camry</model>
            <clearance>7.98</clearance>
        </Car>
    </CarShowroom>
    """

    def get_xml(self):
        return self.xml


# Xml parser
class Parse():
    name: str
    model: str
    clearance: float

    xml = Xml()
    bs = BeautifulSoup(xml.get_xml(), 'xml')

    def get_tag_count(self, tag) -> str:  # return tag len/count <Car>
        count = len(self.bs.find_all(tag))
        string = f'count tag <Car>: {count}'
        return string

    def get_data(self):
        for item in self.bs.findAll("Car"):
            try:
                name = str(item.find("name").text)
                model = str(item.find("model").text)
                clearance = float(item.find("clearance").text)
                print(f'name={name}\tmodel={model}\tclearance={clearance}')
            except ValueError as err:
                """ Это, конечно, не правильная проверка на валидацию, а костыль.
                Доработаю/Обновлю - запушу повторно. """
                print(f'\n❌ ERROR: {err}')


# ==== Call ==== #
prs = Parse()
print(prs.get_tag_count('Car'))
prs.get_data()

# ==== Output ==== #
# count tag <Car>: 2
# name=BMW	model=F5 CS	clearance=10.58
# name=Toyota	model=Camry	clearance=7.98
