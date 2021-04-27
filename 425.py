import gg

a = gg.Dog('Dog',30,12)
print(a.name, 'bmi:', a.bmi())

b = gg.Cat('Cat',25,11.5,3,2,3)
print(b.name, 'bmi:', b.bmi())
b.BWN()

c = gg.Brid('Brid',20,10, True)
print(c.name, 'bmi:', c.bmi())
c.description()

