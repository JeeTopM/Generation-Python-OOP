"""
Нередко в разных странах используются разные форматы дат. Рассмотрим часть из них:
код страны	формат даты
ru	DD.MM.YYYY
us	MM-DD-YYYY
ca	YYYY-MM-DD
br	DD/MM/YYYY
fr	DD.MM.YYYY
pt	DD-MM-YYYY
Реализуйте класс DateFormatter, экземпляры которого позволяют преобразовывать даты в формат определенной страны из таблицы выше.
    При создании экземпляра класс должен принимать один аргумент:
        country_code — код страны
Экземпляр класса DateFormatter должен являться вызываемым объектом и принимать один аргумент:
    d — дата (тип date)
Экземпляр класса DateFormatter должен возвращать строку с датой d в формате страны с кодом country_code.
"""
from datetime import date


class DateFormatter:
    def __init__(self, country_code):
        self.country_code = country_code

    def __call__(self, date):
        if self.country_code == 'ru':
            return date.strftime('%d.%m.%Y')  # DD.MM.YYYY
        elif self.country_code == 'us':
            return date.strftime('%m-%d-%Y')  # MM-DD-YYYY
        elif self.country_code == 'ca':
            return date.strftime('%Y-%m-%d')  # YYYY-MM-DD
        elif self.country_code == 'br':
            return date.strftime('%d/%m/%Y')  # DD/MM/YYYY
        elif self.country_code == 'fr':
            return date.strftime('%d.%m.%Y')  # DD.MM.YYYY
        elif self.country_code == 'pt':
            return date.strftime('%d-%m-%Y')  # DD-MM-YYYY



if __name__ == '__main__':
    # test 1
    ru_format = DateFormatter('ru')
    print(ru_format(date(2022, 11, 7)))  # 07.11.2022

    # test 2
    us_format = DateFormatter('us')
    print(us_format(date(2022, 11, 7)))  # 11-07-2022

    # test 3
    ca_format = DateFormatter('ca')
    print(ca_format(date(2022, 11, 7)))  # 2022-11-07
