#!/usr/bin/python3
#-*- coding: utf-8 -*-
from pyclbr import Function

# атрибут тэга - словарь.
# текстовое представление объекта можно получить str(x) или repr(x).
# Отличие - первое для человека, второе - только scsii-символы.
# Но на практике не всегда соблюдается.

__all__ = ('Node', )

class Node(object):
    
    __AllNodes = {}             # создали узел - добавили в словарь.
                                # здесь содержатся элементы, которые могут понадобиться
    
    def __init__(self, xml_el):         # ����������� ����� ����������� �� xml-����
        self.__OsmId = int(xml_el.get('id'))     
        self.__Lon = float(xml_el.get('lon'))
        self.__Lat = float(xml_el.get('lat'))
        
        self.__Tags = {}
        for tag in xml_el.findall('tag'):
            key = tag.get('k')
            value = tag.get('v')
            self.__Tags[key] = value
            #self.__Tags[ tag['k'] ] = tag['v'] # написали более понятно
            
    osm_id = property(lambda self: self.__OsmId)
    lon = property(lambda self: self.__Lon)
    lat = property(lambda self: self.__Lat)
    
    def __str__(self):
        return 'Node: {0.osm_id} Lat = {0.lat} Lon = {0.lon}'.format(self)       # операция формата может выковыривать свойство из объекта

    def p(self):
        return self.__OsmId, self.__Lon, self.__Lat
    
    
    @classmethod                # функция перестала быть методом экземпляра класса, а стала методом класса => меняем self на cls
    def create(cls,xml_el):    
        '''Factory function'''
        osm_id = int(xml_el.get('id'))
        try :
            return cls.__AllNodes[osm_id]
        except KeyError:
            R = Node(xml_el)
            cls.__AllNodes[osm_id] = R
            return R
    

        
        
        
        
        
        
        
        
        
        
        