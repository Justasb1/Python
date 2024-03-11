class Robotai:
    name = None
    age = None
    enable = None

class Kazkas:
    pass

dulkiuSiurblys = Robotai()
print(type(dulkiuSiurblys))
print(dulkiuSiurblys)
print(dulkiuSiurblys.__dict__)
dulkiuSiurblys.name = 'Xiomi'
dulkiuSiurblys.age = 3
dulkiuSiurblys.enable = True
print(dulkiuSiurblys.__dict__)
dulkiuSiurblys.age = 4

print(Robotai.__dict__)
print(type(dulkiuSiurblys) == Robotai)

print(isinstance(dulkiuSiurblys, Robotai))
print(isinstance(dulkiuSiurblys, Kazkas))


dulkiuSiurblys.color = 'Black'
print(dulkiuSiurblys.__dict__)

Robotai.force = '2kW'

languBotas = Robotai()

setattr(Robotai, 'wheels', 3)

print(dulkiuSiurblys.color)
# print(dulkiuSiurblys.Smulkinti)
ats = 'Deja tokios info neturime'
print(getattr(Robotai, 'force', ats))
print(getattr(Robotai, 'smulkinti', ats))

print(Robotai.__dict__)
del Robotai.force
print(Robotai.__dict__)

#hasattr
#delattr
if hasattr(dulkiuSiurblys, 'name'):
    print(f'dar kol kas turime savybe "name"')
    del dulkiuSiurblys.name
else:
    print ('Tokios savybes nera')