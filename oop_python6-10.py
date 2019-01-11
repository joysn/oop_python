class InstanceCounter(object):
    count = 0

    def __init__(self,val):
        self.val = val
        InstanceCounter.count += 1

    def set_val(self,newval):
        self.val=newval

    def get_val(self):
        return self.val

    def get_count(self):
        return InstanceCounter.count

a = InstanceCounter(5)
b = InstanceCounter(13)
c = InstanceCounter(17)

for obj in(a,b,c):
    print("val of obj: %s" % (obj.get_val()))
    print("count: %s"% (obj.get_count()))
    print("count(from instance): %s" % (obj.count))

# Output
# val of obj: 5
# count: 3
# count(from instance): 3
# val of obj: 13
# count: 3
# count(from instance): 3
# val of obj: 17
# count: 3
# count(from instance): 3
# Traceback (most recent call last):
#   File "oop_python6.py", line 26, in <module>
#     Output
# NameError: name 'Output' is not defined
# [my_machine oop_python]$

class Date(object):
    def get_date(self):
        return '2014-10-13'

class Time(Date):
    def get_time(self):
        return '08:13:07'


dt = Date()
print(dt.get_date())

tm = Time()
print(tm.get_time())
print(tm.get_date())

# Output
# 2014-10-13
# 08:13:07
# 2014-10-13
# [my_machine oop_python]$


# Inheritance

class Animal(object):
    def __init__(self,name):
        self.name = name

    def eat(self,food):
        print('{} is eating {}'.format(self.name,food))

class Dog(Animal):
    def fetch(self,thing):
        print('{} goes after the {}'.format(self.name,thing))

class Cat(Animal):
    def swatstring(self):
        print('{} shreds the string!'.format(self.name))

r = Dog('Rower')
f = Cat('Fluffy')

r.fetch('paper')
f.swatstring()
r.eat('dog food')
f.eat('cat food')
r.swatstring()


# Output
# Rower goes after the paper
# Fluffy shreds the string!
# Rower is eating dog food
# Fluffy is eating cat food
# Traceback (most recent call last):
#   File "oop_python8.py", line 25, in <module>
#     r.swatstring()
# AttributeError: 'Dog' object has no attribute 'swatstring'
# [my_machine oop_python]$

# Inheritance

class Animal(object):
    def __init__(self,name):
        self.name = name

    def eat(self,food):
        print('{} eats {}'.format(self.name,food))

class Dog(Animal):
    def fetch(self,thing):
        print('{} goes after the {}'.format(self.name,thing))

    def show_affecton(self):
        print('{}, wags tail'.format(self.name))

class Cat(Animal):
    def swatstring(self):
        print('{} shreds the string!'.format(self.name))

    def show_affecton(self):
        print('{}, purs'.format(self.name))


for a in (Dog('Rover'), Cat('Fluffy'),Cat('Precious'),Dog('Scout')):
    a.show_affecton()


# Output
# Rover, wags tail
# Fluffy, purs
# Precious, purs
# Scout, wags tail
# [my_machine oop_python]$

import random

class Animal(object):

    def __init__(self,name):
        self.name = name

class Dog(Animal):

    def __init__(self, name):
        super(Dog,self).__init__(name)
        self.breed = random.choice(['Shih Tzu','Beagle','Mutt'])

    def fetch(self,thing):
        print('{} goes after the {}'.format(self.name,thing))


d = Dog('dogname')

print(d.name)
print(d.breed)

# Output
# dogname
# Beagle
# [my_machine oop_python]$
