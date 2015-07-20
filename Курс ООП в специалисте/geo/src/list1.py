#!/usr/bin/python3
#-*- coding: utf-8 -*-

# в итоге нужна совокупность элементов из xml определенного типа
# если есть данные, которые неизвестно, интересны ли - сохранять как есть.

import map  # @ReservedAssignment   - добавляется по ctrl+1 и подавляет у эклипса желание об ошибке
from os.path import abspath, join
import xml.etree.ElementTree as ET
from reportlab.pdfgen import canvas

DataPath = join( '..' , 'data' , 'map.osm' )
DataPath = abspath( DataPath )

print( DataPath )

Doc = ET.parse( DataPath )

Root = Doc.getroot()
for element in Root.findall( 'node' ):
    n = map.Node.create( element )
    # print(n)
    
C = canvas.Canvas( 'map.pdf' )

z0 = 2946000.0 + 6944000.0j
Sc = 0.15

#C.translate(2948000.0, 6947000.0)   # перенос начала координат    
#C.scale(0.01,0.01)

#C.line(2948000.0, 6947000.0, 2949000.0, 6949000.0) # рисуем длинную прямую, чтоб увидеть, рисуется ли хоть что-то
#C.line(0.0, 0.0, 100.0, 100.0)

for el in Root.findall( 'way' ):
    w = map.create_way(el)  # @UndefinedVariable
    print( ' - '.join( str(z) for z in w.proj ))
    
    #path = C.beginPath()
    #P = w.proj
    #z = (next(P) - z0) * Sc # первая точка
    #path.moveTo(z.real, z.imag)
    #for z in P:
    #    z = (next(P) - z0) * Sc
    #    path.lineTo(z.real, z.imag)
    #C.drawPath(path, stroke = True, fill = False)
    
    w.draw( C , origin=z0 , scale=Sc )
    
C.showPage()
C.save()
    
    # параметр bounds в xml-ку задает прямоугольник, в который нужно вписывать