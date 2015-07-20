#!/usr/bin/python3
#-*- coding: utf-8 -*-

__all__ = ('Position', )

from decimal import Decimal

class Position(object):
    def __init__(self, title, unit, count, price=None, summa=None):
        self.__Title = title
        self.__Unit = unit
        self.__Count = Decimal(count)
        self.__Price = None if price == None else Decimal(price)
        if summa == None:
            S = self.count * self.price
            self.__Summa = S.quantize(Decimal('0.01'))
            self.__SumCalculated = True
        else:
            self.__Summa = Decimal(summa)
            self.__SumCalculated = False
            
    #@property
    #def title(self):
    #    return self.__Title
    
    title = property( lambda self : self.__Title)       # то что делает декоратор
                                                    # св-во работает только на чтение
    
    @title.setter
    def title(self, value):
        self.__Title = value
        
    @title.deleter 
    def title(self):
        self.__Title = None
        
    unit  = property( lambda self : self.__Unit )
    count = property( lambda self : self.__Count )
    
    sum_calculated = property( lambda self : self.__SumCalculated)
    
    price  = property( lambda self : self.__Price )
    
    @price.setter 
    def price(self, value):
        self.__sum_calculated = value
        
    @price.setter
    def price(self, value):
        P = Decimal(value)
        if self.sum_calculated:
            self.__Summa = self.count * P
        self.__Price = P
    
   
    @price.deleter                       # Правильно?   
    def price(self):
        self.__Price = None
    
    summa = property( lambda self : self.__Summa )
    
    @summa.setter
    def summa(self, value):
        self.__SumCalculated = False
        self.__Summa = Decimal(value)
 
    # TODO удаление суммы. (означает перевычисление)
    
    
    def as_text(self):
        return '{0},{1},{2},{3},{4}'.format(self.title,self.unit,self.count,self.price,self.summa)
    
    