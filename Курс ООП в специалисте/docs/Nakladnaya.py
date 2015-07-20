#!/usr/bin/python3
#-*- coding: utf-8 -*-

from datetime import datetime
from decimal import Decimal

class Nakladnaya(object):                   # накладная здесь с такими методами = список
    
    # def __new__(cls,...):                  # метод класса
    # ...
    
    def __init__(self, number = None, adate = None):              # инициализация класса. __init__ назвали "конструктором", что не логично.
                                                                       # если adate = datetime.today(), то датавремя присвоится в момент создания программы
        if not number :
            raise NotImplementedError('auto-generated number is not implemented')
        self.__Number = number
        self.__Date = adate if adate else datetime.today()
        self.__Positions = []
        
    # def __del__(self):                      # функция удаления. на самом деле вычищает мусор за объектом. выполняется, когда объект уничтожается сборщиком мусора, а не когда мы вызываем del.
      #   pass                                  # уничтожая экз-р класса сборщик мусора уничтожит связанные объекты. но если одна позиция вдруг вставиться в две наклвдные, то она уничтожена не будет.
    
    @property                                 # стандартный декоратор свойства
    def date(self):                           # создание функции, считывающей значение свойства
        return self.__Date
        
    @date.setter
    def date(self, value):                  # запись свойства
        self.__Date = value
        
    @property
    def number(self):
        return self.__Number
        
    @number.setter
    def number(self, value):
        self.__Number = value
    
    def add_position(self, title, unit, count, price = None, summa = None):
        count = Decimal(count)
        if summa == None:
            summa = (count * Decimal(price)).quantize(Decimal('0.01'))
        self.__Positions.append((title, unit, count, price, summa))

    def del_posision(self,idx):
        del self.__Positions[idx]
        
    def get_posision(self,idx):
        return self.__Positions[idx]
        
    def as_txt(self):
        L = []
        L.append('Номер={0}'.format(self.number))
        L.append('Дата={0}'.format(self.date))            # писать здесь переменную в функции в общем случае ошибка
        for no, pos in enumerate(self.__Positions, 1):
            L.append('Позиция={0},{1}'.format(no, self.__Positions))
        return '\n'.join(L)                                # сцепка через разделитель
        
    def subscribe(self):
        raise NotImplementedError('Nakladnaya.subscribe')