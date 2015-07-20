#/usr/bin/python3
#-*- coding: utf-8 -*-

from nakladnaya import Nakladnaya

doc = Nakladnaya('12')
doc.add_position('Фыфв','шт',12,'23.14')
doc.add_position('Олдж','шт','12.1','100.10')

print (doc.as_text())

doc.number = '100'

print (doc.as_text())
