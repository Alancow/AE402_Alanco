import human

a = human.Human('David',70,180)
print(a.name, 'bmi:', a.bmi())

b = human.Woman('Jerry',55,160,33,26,34)
print(b.name, 'bmi:', b.bmi())
b.BWN()

c = human.MAN('Alan',68,179, True)
print(c.name, 'bmi:', c.bmi())
c.description()