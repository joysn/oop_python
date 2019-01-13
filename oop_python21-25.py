# With Context #

with open('test.txt') as fh:
    for line in fh:
        line = line.rstrip()
        print(line)
print('done!')

fh = open('test.txt')
for line in fh:
    print(line)
fh.close()


class MyClass(object):

    def __enter__(self):
        print('We have entered "with"')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('error type: {}'.format(exc_type))
        print('error value: {}'.format(exc_val))
        print('error traceback: {}'.format(exc_tb))
        print('we are leavin "with"')

    def sayhi(self):
        print('hi, instance {}'.format(id(self)))


with MyClass() as cc:
    cc.sayhi()
    5/0

print('after the with block')

# Output
# This is a silly message
# done!
# This is a silly message
# We have entered "with"
# hi, instance 140292684973840
# error type: <class 'ZeroDivisionError'>
# error value: division by zero
# error traceback: <traceback object at 0x7f98773fed48>
# we are leavin "with"
# Traceback (most recent call last):
#   File "oop_python21.py", line 33, in <module>
#     5/0
# ZeroDivisionError: division by zero


## New Style Classes


# old class
class OldClass():
    pass


# new class
class NewClass(object):
    pass


oc = OldClass()
nc = NewClass()

print(type(oc))
print(type(nc))
print(oc.__class__)

# Output
# <class '__main__.OldClass'>
# <class '__main__.NewClass'>
# <class '__main__.OldClass'>
# [my_machine oop_python]$

# Exception Handling

import re
mydict = {'a':1, 'b':2, 'c':3, 'd':4}
key = input('please input a key: ')

try:
    print('testing for error')
    print('the value for {0} is {1}'.format(key, mydict[key]))

except (KeyError, ValueError) as e:
    #print(dir(e))
    print('trapped error {0} {1}'.format(e.args, e.with_traceback))
    print("the key "+ key + " does not exist")

print("program continues...")

def process_date(this_date):

    if not re.search(r'^\d\d\d\d-\d\d-\d\d$', this_date):
        raise ValueError('Please submit a date in YYYY-MM-DD format')

    print('the submited date is {0}',format(this_date))

process_date('1980-01-03')
process_date('10/10/1985')


# output
# lease input a key: z
# testing for error
# trapped error ('z',) <built-in method with_traceback of KeyError object at 0x7f479cab34c0>
# the key z does not exist
# program continues...
# the submited date is {0} 1980-01-03
# Traceback (most recent call last):
#   File "oop_python23.py", line 26, in <module>
#     process_date('10/10/1985')
#   File "oop_python23.py", line 21, in process_date
#     raise ValueError('Please submit a date in YYYY-MM-DD format')
# ValueError: Please submit a date in YYYY-MM-DD format
# [my_machine oop_python]$

class MyError(Exception):
    def __init__(self,*args):

        print('calling init')
        if args:
            self.message = args[0]
        else:
            self.message = ''

    def __str__(self):
        print('calling str')
        if self.message:
            return "here is a Myerror exception with a message {0}".format(self.message)
        else:
            return "here is MyError exception"

#raise MyError
raise MyError('Houston, we have a problem')

# Output
# calling init
# Traceback (most recent call last):
#   File "oop_python24.py", line 18, in <module>
#     raise MyError('Houston, we have a problem')
# calling str
# __main__.MyError: here is a Myerror exception with a message Houston, we have a problem
# [my_machine oop_python]$

	
# Serialization
import pickle

class MyClass(object):

    def __init__(self, init_val):
        self.val = init_val
    def increment(self):
        self.val += 1

cc = MyClass(5)
cc.increment()
cc.increment()

my_int = 555
my_str = 'oh my goodness'
my_list = ['a','b','c','d']
my_dict = {'a':1,'b':2}

with open('pickledata.txt','wb') as fh:
    #pickle.dump((my_int,my_str,my_list,cc,my_dict),fh)
    pickle.dump( my_dict, fh)

with open('pickledata.txt','rb') as fh:
    unpickledlist = pickle.load(fh)


print(type(unpickledlist))
for key in unpickledlist.keys():
    print(key,unpickledlist[key])
print(unpickledlist[0])
print(unpickledlist[1])
print(unpickledlist[2])
print(unpickledlist[3])
print(unpickledlist[3].val)


"""
# Ouput
# ['a', 'b', 'c', 'd']
# [my_machine oop_python]$


## JSON
import json

with open('backup_config.json') as fh:
        conf = json.load(fh)
print(conf)
print(type(conf))

conf['newkey'] = 5.0005

with open('backup_config.json','w') as fh:
    json.dump(conf,fh)

## YAML

import yaml

mydict = {'a':1, 'b':2, 'c': 3}
mylist = [1,2,3,4,5]
mytuple = ('x','y','z')

myobj = (
    [1,2,3,4,5],
    {'a':1, 'b':2,'c':3},
    [
        {'x':98,'y':99, 'z': 100 },
        3,
        4
    ],
    {'a':[1,2,3], 'b': [4,5,6],'c':[7,8,9]}
)

loaded_yaml = yaml.dump(mydict,default_flow_style=False)
print(loaded_yaml)
print(yaml.dump(mylist, default_flow_style=False))
print(yaml.dump(mytuple, default_flow_style=False))
print(yaml.dump(myobj, default_flow_style=False))

# a: 1
# b: 2
# c: 3
#
# - 1
# - 2
# - 3
# - 4
# - 5
#
# !!python/tuple
# - x
# - y
# - z
# !!python/tuple
# - - 1
#   - 2
#   - 3
#   - 4
#   - 5
# - a: 1
#   b: 2
#   c: 3
# - - x: 98
#     y: 99
#     z: 100
#   - 3
#   - 4
# - a:
#   - 1
#   - 2
#   - 3
#   b:
#   - 4
#   - 5
#   - 6
#   c:
#   - 7
#   - 8
#   - 9

"""
