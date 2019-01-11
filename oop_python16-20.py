# Different Inhertance methods
import abc

class GetSetParent(object):
    __metaclass__ = abc.ABCMeta
    def __init__(self,value):
        self.val = 0

    def set_val(self,value):
        self.val = value

    def get_val(self):
        return self.val

    @abc.abstractmethod
    def showdoc(self):
        return

class GetSetInt(GetSetParent):

    # Specialing - Extend
    def set_val(self,value):
        if not isinstance(value,int):
            value = 0
        super(GetSetInt,self).set_val(value)

    #Provide - Implement
    def showdoc(self):
        print('GetSetInt object ({}), only accepts '
              'integer values'.format(id(self)))


class GetSetList(GetSetParent):
    def __init__(self,value=0):
        self.vallist = [value]
    # Override
    def get_val(self):
        return self.vallist[-1]
    #Special method
    def get_vals(self):
        return self.vallist
    def set_val(self,value):
        self.vallist.append(value)
    # Provide
    def showdoc(self):
        print('GetSetList object, len {}, stores history of value set'.format(len(self.vallist)))


x = GetSetInt(3)
x.set_val(5)
print(x.get_val())
x.showdoc()

gsl = GetSetList(5)
gsl.set_val(10)
gsl.set_val(20)
print(gsl.get_val())
print(gsl.get_vals())
gsl.showdoc()


# Output
# 5
# GetSetInt object (140059149858800), only accepts integer values
# 20
# [5, 10, 20]
# GetSetList object, len 3, stores history of value set
# [my_machine oop_python]$

# Composition

import random
from io import StringIO

class WriteMyStuff(object):

    def __init__(self, writer):
        self.writer = writer

    def write(self):
        write_text = "This is a silly message"
        self.writer.write(write_text)

fh = open('test.txt','w')
w1 = WriteMyStuff(fh)
w1.write()
fh.close()

sioh = StringIO()
w2 = WriteMyStuff(sioh)
w2.write()


print('file object: ',open('test.txt','r').read())
print('StringIO Object: ',sioh.getvalue())

# Output
# file object:  This is a silly message
# StringIO Object:  This is a silly message
# [my_machine oop_python]$

# Advanced Topics
# CORE Syntax Resolution

class SumList(object):

    def __init__(self,this_list):
        self.my_list = this_list

    # called automatically with +
    def __add__(self,other):

        new_list = [ x+y for x,y in zip(self.my_list,other.my_list)]
        return SumList(new_list)

    # Called automatically with print
    def __repr__(self):
        return str(self.my_list)


cc = SumList([1,2,3,4,5])
dd = SumList([100,200,300,400,500])

ee = cc + dd  ## cc.__add__(dd)
print(ee)


# Output
# [101, 202, 303, 404, 505]
# [my_machine oop_python]$

# Inheriting from builtins classes


class MyDict(dict):
    def __setitem__(self, key, val):
        print("setting a key and value!")
        dict.__setitem__(self, key, val*2)


dd = MyDict()
dd['a'] = 5
dd['b'] = 6

for k in dd.keys():
    print('{}={}'.format(k, dd[k]))


class MyList(list):

    def __getitem__(self, index):
        if index == 0: raise IndexError
        if index > 0: index = index - 1
        return list.__getitem__(self, index)

    def __setitem__(self, index, value):
        if index == 0: raise IndexError
        if index > 0: index = index - 1
        list.__setitem__(self, index, value)


x = MyList(['a', 'b', 'c'])  # __init__() inherited from builtin class
print(x)                     # __repr__() inherited from builtin class
x.append('spam')             # append() inherited from builtin class
print(x[1])
print(x[4])

# Output
# setting a key and value!
# setting a key and value!
# a=10
# b=12
# ['a', 'b', 'c']
# a
# spam
# [my_machine oop_python]$


# @property decorator
# internal attributes starts with _

class GetSet(object):

    instance_count = 0

    __mangled_name = 'no privacy!'

    def __init__(self, value):
        self._attrval = value  # Variable name preceeded by _ to be used by internal class only
                               # But not enforced

    @property
    def var(self):
        print("getting the var attribute")
        return self._attrval

    @var.setter
    def var(self, value):
        print("setting the var attribute {}".format(value))
        self._attrval = value

    @var.deleter
    def var(self):
        print("deletin the var attribute")
        self._attrval = None

me = GetSet(5)
me.var = 1000
print(me.var)
del me.var
print(me.var)

# Output
# setting the var attribute 1000
# getting the var attribute
# 1000
# deletin the var attribute
# getting the var attribute
# None
# setting the var attribute 10
# 10
# Traceback (most recent call last):
#   File "oop_python20.py", line 38, in <module>
#     print(cc.__mangled_name)  # So should not be used by subclasses
# AttributeError: 'GetSet' object has no attribute '__mangled_name'
# [my_machine oop_python]$


cc = GetSet(5)
cc.var = 10
print(cc._attrval) ## Provacy is not enforced
print(cc.__mangled_name)  # So should not be used by subclasses
print(cc._GetSet__mangled_name)
