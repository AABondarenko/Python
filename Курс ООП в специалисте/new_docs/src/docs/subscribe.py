#!/usr/bin/python3
#-*- coding: utf-8 -*-

# ��� ������� �������� �����������, ���������� ����������.
# 
# 
# 
# 
# 
# 
# 
# 
# 

__all__ = ( 'DocumentIsSubscribed',
           'subscribable',
           'unsubscribed_only' )

class DocumentIsSubscribed (Exception):         # ����������� ����� ����������
    pass


def subscribable(cls):
    
    AttrName = '_{0}__Subscribed'.format(cls.__name__)  # чтобы инт-тор не думал, что 
                                                        # мы нарушаем пр. инкапсуляции
    
    if not hasattr(cls, 'assess_unsubscribed'):           # проверили, есть ли такая функция
        def assess_unsubscribed(self):
            if self.is_subscribed:
                raise DocumentIsSubscribed('Document is subscribed')

        setattr(cls, 'assess_unsubscribed', assess_unsubscribed)
    
    old_init = getattr(cls, '__init__',None)   # выдергиваем из класса ссылку на ф-цию __init__
    def __init__(self, *args, **kwargs):        # создаем новый конструктор
        if old_init : old_init(self, *args, **kwargs)  # если конструктор был, мы его вызываем
        if not hasattr(self, AttrName):
            setattr(self, AttrName, False)
    
    setattr(cls, '__init__', __init__)
    
    if not hasattr(cls, 'subscribe'):
        def subscribe(self):
            setattr(self, AttrName, True)
        setattr(cls, 'subscribe', subscribe)
        
    # TODO написать метод unsubscribe
    
    if not hasattr(cls, 'is_subscribed'):
        P = property(lambda self: getattr(self, AttrName))
        setattr(cls, 'is_subscribed', P)
    
    return cls
    
def unsubscribed_only(function):            # ДЕКОРАТОР. Смысл использования не технический, а содержательный в данном случае.
                                            # "Пляски вокруг превратились в пляски вокруг и мы можем созерцать чистые функции"
    def checked_func(self, *args, **kwargs):
        self.asess_unsubscribed()
        return function(self, *args, **kwargs)
    return checked_func



    