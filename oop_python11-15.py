#Multiple Inhertance

class A(object):

    def dothis(self):
        print('doing this in A')

class B(A):
    pass

class C(object):

    def dothis(self):
        print('doing this in C')

class D(B,C):
    pass


d_inst = D()
d_inst.dothis()

print(D.mro())


# Output
# doing this in A
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.C'>, <class 'object'>]
# [my_machine oop_python]$

## Diamond inhertance

class A(object):

    def dothis(self):
        print('doing this in A')

class B(A):
    pass

class C(A):

    def dothis(self):
        print('doing this in C')


class D(B,C):
    pass

d_inst = D()
d_inst.dothis()

print(D.mro())
# Output
# doing this in C
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
# [my_machine oop_python]$

# Class Methods

class InstanceCounter(object):
    count = 0

    def __init__(self, val):
        self.val = val
        InstanceCounter.count += 1

    def set_val(self, newval):
        self.val = newval

    def get_val(self):
        return self.val

    @classmethod
    def get_count(cls):
        return cls.count


a = InstanceCounter(5)
b = InstanceCounter(13)
c = InstanceCounter(17)


for obj in(a,b,c):
    print("val of obj: %s" % (obj.get_val()))
    print("count: %s"% (obj.get_count()))
    print("count(from instance): %s" % (obj.count))
print("Calling from Class iteslf: %s" % (InstanceCounter.get_count()))

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
# Calling from Class iteslf: 3
# [my_machine oop_python]$

# Static Method
class InstanceCounter(object):
    count = 0

    def __init__(self,val):
        self.val = self.filterint(val)
        InstanceCounter.count += 1


    @staticmethod
    def filterint(value):
        if not isinstance(value,int):
            return 0
        else:
            return value

a = InstanceCounter(5)
b = InstanceCounter(13)
c = InstanceCounter(17)
d = InstanceCounter('hi')

print(a.val , b.val, c.val, d.val)



# Output
# 5 13 17 0
# [my_machine oop_python]$


# Abstract Class

import abc

class GetterSetter(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def set_val(self,input):
        return

    @abc.abstractmethod
    def get_val(self):
        return

class MyClass(GetterSetter):

    def set_val(self,input):
        self.val = input

    def get_val(self):
        return(self.val)


x = MyClass()
print(x)

# Output
# <__main__.MyClass object at 0x7f106c99f2e8>
# [my_machine oop_python]$
