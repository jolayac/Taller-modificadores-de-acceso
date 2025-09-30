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
print(hasattr(a, '__secret'), hasattr(a, '_A__secret'))  # False True
'''

# 4) Lectura de código
'''


class Base:
    def __init__(self):
        self._token = "abc"


class Sub(Base):
    def reveal(self):
        return self._token


print(Sub().reveal())
'''

# 5) Name mangling en herencia
'''
class Base:
    def __init__(self):
        self.__v = 1            # __v se transforma a _Base__v por el mangling.


class Sub(Base):
    def __init__(self):
        # se llaman a los aributos de la superclase (Base).
        super().__init__()
        self.__v = 2

    def show(self):
        return (self.__v, self._Base__v)


print(Sub().show())
'''

# 6) Identifica el error
'''
class Caja:
    __slots__ = ('x',)  # Esto dice


c = Caja()
c.x = 10
c.y = 20
'''

# 7) Rellenar espacios

'''
class B:
    def __init__(self):
        self._numero = 99

b = B()
print(b._numero)
'''

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
print(hasattr(m, '_step'),      # True 
    hasattr(m, '__tick'),       # False
    hasattr(m, '_M__tick'))     # True
''''''
hasattr (corto para has attribute).Return whether the object has an attribute with the given name.
This is done by calling getattr(obj, name) and catching AttributeError.
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
