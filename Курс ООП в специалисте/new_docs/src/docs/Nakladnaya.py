#!/usr/bin/python3
#-*- coding: utf-8 -*-

# накладная спископодобный объект. для этого нужно позволить
# себе писать len(doc), doc[2], del doc[2], append.doc и цикл for для перебора.
# почти везде, где питон ждет списка можно подставить накладную.
# "метод утиной типизации"

# после того, как накладная подписана, ничего менять в ней нельзя.

# считаем, что одна позиция может иметься в нескольких накладных. тогда нужна
# защита от изменений в подписанной накладной. Можно сделать красиво, но
# сделаем грубо.

# по регламенту подпись может быть отозвана, причем отдельной процедурой.
# считаем, что документы подписываются одним лицом. 

__all__ = ('Nakladnaya', )

from .subscribe import subscribable, unsubscribed_only
from datetime import datetime
from reportlab.pdfgen import canvas         # классы для отрисовки
#from decimal import Decimal

from .Position import Position

@subscribable                               # ПРИМЕСЬ
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
        
    @date.setter                            # setter надо наверх
    @unsubscribed_only
    def date(self, value):
        # self.assess_unsubscribed()          # функции проверки подписи. Превратили в декоратор
        self.__Date = value
        
    @property
    def number(self):
        return self.__Number
        
    @number.setter
    @unsubscribed_only
    def number(self, value):
        # запретить изменять номер у подписанного д-та:
        #self.assess_unsubscribed()
        self.__Number = value
    
    
    # !TODO если функцию надо вставлять много где,
    # надо делать декоратор @assess_unsubscribed
    #def add_position(self, title, unit, count, price = None, summa = None):
    
    @unsubscribed_only
    def append(self, *args, **kwargs):
        # self.assess_unsubscribed()        # вместо нее сделали декоратор
        if isinstance(args[0], Position):   # если args[0] - экземпляр класса
            P = args[0]
        else:
            P = Position( *args, **kwargs )
        #count = Decimal(count)
        #if summa == None:
        #    summa = (count * Decimal(price)).quantize(Decimal('0.01'))
        #self.__Positions.append((title, unit, count, price, summa))
        self.__Positions.append(P)
        
        
        
    def __delitem__(self,idx):
        del self.__Positions[idx]
        
    def __getitem__(self,idx):          # спец объект выдергивает позицию
        return self.__Positions[idx]
    
    def __len__(self):
        return len(self.__Positions)
    
    def __iter__(self):                 # берет объект и возвращает последовательность, которую можно перебрать 1 раз. можно несколько раз ф-цию вызвать.
        return iter(self.__Positions)
    
    # def __setitem__(self): - эту возможность для накладной не делаем
        
    def as_txt(self):
        L = []
        L.append('Номер={0}'.format(self.number))
        L.append('Дата={0}'.format(self.date))            # писать здесь переменную здесь в функции в общем случае ошибка
        for no, pos in enumerate(self, 1):
            L.append('Позиция={0},{1}'.format(no, pos.as_text()))
        return '\n'.join(L)                                # сцепка через разделитель
        
    #def subscribe(self):    #теперь он из примеси
    #    raise NotImplementedError('Nakladnaya.subscribe')
    
    def save_as_pdf(self, filename):
        W = 200.0
        H = 300.0
        CP = 270.0          # текущая позиция
        C = canvas.Canvas(filename)                     # для отправки на принтер нужно создать временный файл
        Step = 10
        
        C.drawString(0, CP, 'Накладная № {0}'.format(self.number))
        CP -= Step                  # движемся сверху-вниз
        
        C.drawString(0, CP, 'Дата {0}'.format(self.date))
        CP -= Step
        
        for no, pos in enumerate(self, 1):
            C.line(0, CP, W, CP)
            C.drawString(0, CP, '{0}, {1}'.format(no, pos.as_text()))
            CP -= Step
        
        C.showPage()                # переворачивает страницу. Неперевернутая страница не будет сохранена
        C.save()
    
    #################################################################
    
    # БЫЛ ВРЕМЕННЫЙ КОД.
    
    
#def test(self):
#    print("Test: {0}".format(self.number))
    
# Nakladnaya.test = test - так можно добавить ф-цию в класс

#setattr(Nakladnaya, 'test', test)  # добавить ф-цию в класс по-человечески
                                    # лучше 2 и 3 аргумент одинаковые
                                    # проще будет отлаживать
# если метод уже есть, он затрется добавляемым



