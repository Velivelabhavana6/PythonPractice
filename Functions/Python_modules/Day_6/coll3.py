from collections import namedtuple
Dog=namedtuple('Dog',['age','Breed'])
Tom=Dog(age=6,Breed='Husk')
print(Tom)
print(Tom.age)