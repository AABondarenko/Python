#!/usr/bin/python3
#-*- coding: utf-8 -*-

__all__ = ('Way', )

class Way(object):
    
    __ways = {}
    
    def __init__(self, xml_el):
        self.__ways.update(xml_el.attrib)                                   # засунули в словарь все атр-ты тега way. ref там нету
        self.__ways['ref']=list()                                           # список как значение ключа в словаре
        for child in xml_el:
            self.__ways['ref'].append(child.get('ref'))                     # берем все значения ref из way и засовываем в список
            
    def get_id(self):
        return self.__ways.get('id')

    def refs(self):
        return self.__ways['ref']
            


        
        
# создать класс для контура
# про контур нужен ай ди
# все что сверху сохранять как есть
# не нужно внутри контура хранить узлы

# взять узел из словаря, выдернуть координаты и сохранить в контур
# найти простой способ

