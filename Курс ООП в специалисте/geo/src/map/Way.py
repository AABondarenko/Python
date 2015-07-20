#!/usr/bin/python3
#-*- coding: utf-8 -*-

__all__ = ('Way', )

import pyproj
from .node import Node

class Way(object):
    
    __AllWays = {}
    
    def __init__(self, xml_el, tags):
        self.__OsmId = int(xml_el.get('id'))
        self.__Path = []
        for nd in xml_el.findall('nd'):
            OsmId = int(nd.get('ref'))
            node = Node.get(OsmId)
            data = (node.lat, node.lon)
            self.__Path.append(data)
            
        self.__Tags={}
        self.__Tags.update(tags)
        
        # TODO сделать примесью (потому что одна и та же работа)
        # хранение тэгов как в классе Node
        # В смысле переделать то что ниже (перенесли в create)
  
    osm_id = property( lambda self : self.__OsmId )
    
    def __iter__( self ):             # сам экземпляр можно использовать как последовательность
        return iter( self.__Path )
    
    # если у объекта есть __iter__, то его можно ставить в цикл for.
    # перебор в общем виде.
    @property           # не обязательно делать свойством
    def proj( self ):
        return WayIterator( self.__Path )
    
    # пример СТАТИЧЕСКОГО МЕТОДА в классе:
    @staticmethod           # иногда удобно, например чтоб не забивать пространство имен
    def s_example():
        pass
    
    stroke_color = property( lambda self : (0.9, 0.9, 0.9) )   # возвращает цвет в виде кортежа
    fill_color =   property( lambda self : None            )
    line_width =   property( lambda self : 0.1             )
    
    # отрисовка контура одной командой
    def draw( self , canvas , origin = 0j , scale = 1.0 ):
        canvas.saveState()          # уборка мусора
        try:                        # чтоб потом восстановить рисовалку по умолчанию, если что-то произойдет
            try:
                canvas.setStrokeColorRGB(*self.stroke_color)
            except TypeError:
                Stroke = False
            else:
                Stroke = True
            try:
                canvas.setFillColorRGB(*self.fill_color)
            except TypeError:
                Fill = False
            else:
                Fill = True
            canvas.setLineWidth(self.line_width)
            draw_path = canvas.beginPath()
            seq = self.proj
            z = (next(seq) - origin) * scale
            draw_path.moveTo(z.real, z.imag)
            for z in seq:
                z = (z - origin)*scale
                draw_path.lineTo(z.real, z.imag)
            canvas.drawPath(draw_path, stroke = Stroke, fill = Fill)
        finally:
            canvas.restoreState() 

# сооружаем свой итератор (for). "притянутый за уши".
# итератор обязан содержать как минимум ф-цию __next__.
# и как правило содержит еще __init__ и __iter__
class WayIterator(object):
        
    def __init__(self, coords):
        self.__Coords = coords
        self.__Index  = 0
        self.__Proj   = pyproj.Proj(proj = 'utm', ellps = 'WGS84')      # посмотрели в книжке. для конкретных регионов эллипсоид м.б. другой.
        
        
    def __iter__(self):             # та функция в итераторе именно в таком виде
        return self
        
    def __next__(self):             # ссылка на следующий элемент последовательности. Итератор - это много раз вызванная нэкст.
                                    # когда ничего не осталось, ф-ция нэкст должна выкидывать исключение (по умолч будет индекс эррор), или то что нам нужно
        try:
            lat, lon = self.__Coords[self.__Index]
            self.__Index += 1
            x, y = self.__Proj(lon, lat)
            return complex(x,y)
        except IndexError as Exc:
            raise StopIteration() from Exc
                
            
        
        
        
        
        
        
        
        
        