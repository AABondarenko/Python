#!/usr/bin/python3
#-*- coding: utf-8 -*-

import docs


Doc = docs.Nakladnaya('12')
Doc.append('Рога', 'шт', 12, '23.13')
Doc.append('Копыта', 'кг', '12.1', '100.10')

Doc.subscribe()

#Doc.number = '777'

print(Doc.as_txt())
print('________________________________')

Doc.save_as_pdf('test.pdf')

# print(Doc.test.__name__)

#Doc.number = '1000'
#print(Doc.as_txt())





# Doc = Nakladnaya()                          # () - вызов ф-ции. Класс - функтор

# Doc.inst_method()                           # вызов метода экземпляра. интерпретатор видит Nakladnaya.inst_method(Doc)

# Nakladnaya.class_method()                   # вызов метода класса. интерпретатор видит Nakladnaya.class_method(Nakladnaya)
# Doc.class_method() - тоже можно