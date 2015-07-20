#!/usr/bin/python3
#-*- coding: utf-8 -*-

# в итоге нужна совокупность элементов из xml определенного типа
# если есть данные, которые неизвестно, интересны ли - сохранять как есть.

import map  # @ReservedAssignment   - добавляется по ctrl+1 и подавляет у эклипса желание говорить об ошибке
from os.path import abspath, join
import xml.etree.ElementTree as ET

DataPath = abspath(join('..', 'data', 'map.osm'))

Doc = ET.parse(DataPath)
Root = Doc.getroot()
nodes_dct={}

for element in Root.findall('node'):
    n = map.Node.create(element)
    nodes_dct[n.osm_id] = list()
    nodes_dct[n.osm_id].append(n.lat)
    nodes_dct[n.osm_id].append(n.lon)

print(nodes_dct)

for element in Root.findall('way'):
    w = map.Way(element)

    print('Для way id =' , map.Way.get_id(w), 'есть координаты:', '\nlat          lon')
    
    for elem in map.Way.refs(w):
        try:
            print(nodes_dct[int(elem)])
        except:
            pass
    #k = map.Way.get_id(w)
    #print(ET.tostring(element))
    #print(element.attrib)
    #print(len(k.keys()))
    #print(k)
    
    print('____________________________________')