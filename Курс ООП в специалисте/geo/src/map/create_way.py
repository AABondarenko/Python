#!/usr/bin/python3
#-*- coding: utf-8 -*-

__all__ = ('create_way', )

from .Way import Way
from .Building import Building

# стучимся к переменной класса Way
_AllWaysName = '_{0}__AllWays'.format( Way.__name__ )     # зачем так сложно: а вдруг ссылка побочная
_AllWays = getattr( Way , _AllWaysName )

def create_way( xml_el ):     # это все равно метод класса,
                              # потому что по назначению.
                              # такая штука называется СТАТИЧЕСКИЙ МЕТОД.
                              # др словами, ст метод - такая функция, которую удобно считать методом
    
    OsmId = int( xml_el.get('id') )
        
    Tags = {}
    for tag in xml_el.findall('tag') :
        key       = tag.get('k')
        value     = tag.get('v')
        Tags[key] = value
            
    if OsmId in _AllWays:
        return _AllWays[OsmId]
        
    if Tags.get( 'building' , 'no' ).lower() == 'yes' :     # если гет не нашла билдинг, то подставит no
        del Tags['building']    # возможно удалять не нужно, мы ведь в словарь пихали то, чем не пользуемся
        R = create_building( xml_el , Tags)
    else:
        R = Way( xml_el , Tags )
        
    _AllWays[R.osm_id] = R
    return R

def create_building( xml_el , Tags):
    return Building( xml_el , Tags)
















