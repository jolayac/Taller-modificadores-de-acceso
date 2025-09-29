# Juan Sebastián Olaya Castañeda

# 1) Selección múltiple
'''
class A:
    x = 1
    _y = 2
    __z = 3

a = A()
for n in dir(a):
    print(n)
'''

# 2) Salida del programa
'''
class A:
    def __init__(self):
        self.__secret = 42
a = A()
print(hasattr(a, '__secret'), hasattr(a, '_A__secret')) # False True
'''

# 6) Identifica el error

class Caja:
    __slots__ = ('x',)
    
c = Caja()
c.x = 10
c.y = 20

# 8) Lectura de métodos “privados”
'''
class M:
    def __init__(self):
        self._state = 0
    def _step(self):
        self._state += 1
        return self._state
    def __tick(self):
        return self._step()
m = M()
print(hasattr(m, '_step'), hasattr(m, '__tick'),hasattr(m, '_M__tick')) # True False True
'''

# 10) Comprensión de dir y mangling

'''
class D:
    def __init__(self):
        self.__a = 1
        self._b = 2
        self.c = 3


d = D()
internos = [n for n in dir(d) if 'a' in n]
for n in internos:
    print(n)
'''