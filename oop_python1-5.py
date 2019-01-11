class MyClass(object):
    var = 10


this_obj = MyClass()
print(this_obj.var)

that_obj = MyClass()
print(that_obj.var)

# Output
# 10
# 10
# [my_machine oop_python]$


class Joe(object):
    greeting = "hello, Joe"
    def callme(self):
        print('calling callme with instance')
        print(self)



thisjoe = Joe()

print(thisjoe.greeting)
thisjoe.callme()
print(thisjoe)

# Output
# hello, Joe
# calling callme with instance
# <__main__.Joe object at 0x7f8c8b681cf8>
# <__main__.Joe object at 0x7f8c8b681cf8>
# [my_machine oop_python]$

import random

class MyClass(object):
    def dothis(self):
        self.rand_val = random.randint(1,10)


myinst = MyClass()
myinst.dothis()
print(myinst.rand_val)

##############################################
class MyClass2(object):
    def set_val(self,val):
        self.value = val

    def get_val(self):
        return self.value

a = MyClass2()
b = MyClass2()

a.set_val(10)
b.set_val(100)
a.value = 'hello'

print(a.get_val())
print(b.get_val())

##############################################

class MyInteger(object):
    def set_val(self,val):
        try:
            val = int(val)
        except ValueError:
            return
        self.val = val

    def get_val(self):
        return self.val

    def increment_val(self):
        self.val = sel.val + 1

i = MyInteger()
i.set_val(9)
print(i.get_val())
i.set_val('hi')
print(i.get_val())
i.val = 'hi'
print(i.get_val())
#print(i.increment_val()) ## Error


# Output
# 1
# hello
# 100
# 9
# 9
# hi
# [my_machine oop_python]$

class MyNum(object):
    def __init__(self):
        print('calling __init__')
        self.val = 0

    def increment(self):
        self.val = self.val +1

dd = MyNum()
dd.increment()
dd.increment()
print(dd.val)


class MyNum1(object):
    def __init__(self,val):
        print('calling __init__')
        try:
            val = int(val)
        except ValueError:
            val = 0
        self.val = val

    def increment(self):
        self.val = self.val +1

dd = MyNum1(5)
dd.increment()
dd.increment()
print(dd.val)
dd = MyNum1('hi')
dd.increment()
print(dd.val)


# Output
# calling __init__
# 2
# calling __init__
# 7
# calling __init__
# 1
# [my_machine oop_python]$

class YourClass(object):
    classy = 10

    def set_val(self):
        self.insty = 100


dd = YourClass()
dd.set_val()
print(dd.classy)
print(dd.insty)

class YourClass1(object):
    classy = 'class value!'


dd = YourClass1()
print(dd.classy)
dd.classy = 'inst value!'
print(dd.classy)
del dd.classy
print(dd.classy)



# Output
# 10
# 100
# class value!
# inst value!
# class value!
# [my_machine oop_python]$
