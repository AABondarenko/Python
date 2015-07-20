#/usr/bin/python3
#-*- coding: utf-8 -*-

from datetime import datetime
from decimal import Decimal

class Nakladnaya (object):
    
    # def __new__ (cls, ...):
    #    ......
    
    def __init__ (self, number = None, adate = None, ):
        if not number :
            raise NotImplementedError ('Auto-generated numbers not implemented')
        self.__Date = adate if adate else datetime.today()
        self.__Positions = []
        self.__Number = number
        
    # def __del__ (self):
    #     pass

    @property
    def date (self):
        return self.__Date

    @date.setter
    def date (self, value):
        self.__Date = value

    @property    
    def number (self):
        return self.__Number

    @number.setter
    def number (self, value):
        self.__Number = value
    
    def add_position (self, title, unit, count, price = None, summa = None):
        count = Decimal(count)
        if summa == None:
            summa = (count * Decimal(price)).quantize(Decimal('.01'))
        self.__Positions.append((title, unit, count, price, summa))
    
    def del_position (self, idx):
        del self.__Positions[idx]
    
    def get_position (self, idx):
        return self.__Positions[idx]
        
    def as_text (self):
        L = []
        L.append('Номер={0}'.format(self.number))
        L.append('Дата={0}'.format(self.date))
        for i, pos in enumerate(self.__Positions, 1):
            L.append('Поз{0}={1}'.format(i, pos))
        return '\n'.join(L)
        
    def subscribe (self):
        raise NotImplementedError ('Nakladnaya.subscribe')
       
    
