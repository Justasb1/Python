#__getattribute__

from typing import Any

class Points:
    def __init__(self,x ,y):
        self._x = x
        self._y = y

    def __getattribute__(self, items):
        print('__getattribute__ startavo')
        return
    
    @property
    def x(self):
        print('Kreipiames i savybe x')
        return self._x
    
    @property
    def x(self):
        print('Kreipiames i savybe y')
        return self._y
    
t1 = Points(1, 20)
a = t1.x
print(a)