#!/usr/bin/python3
#-*- coding: utf-8 -*-

from Nakladnaya import Nakladnaya           # фром имя_модуля импорт имя_класса


Doc = Nakladnaya('12')
Doc.add_position('Рога', 'шт', 12, '23.13')
Doc.add_position('Копыта', 'кг', '12.1', '100.10')

print(Doc.as_txt())








# Doc = Nakladnaya()                          # () - вызов ф-ции. Класс - функтор

# Doc.inst_method()                           # вызов метода экземпляра. интерпретатор видит Nakladnaya.inst_method(Doc)

# Nakladnaya.class_method()                   # вызов метода класса. интерпретатор видит Nakladnaya.class_method(Nakladnaya)
# Doc.class_method() - тоже можно