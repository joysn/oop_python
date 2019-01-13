import pdb

value = [1,2,3,4,5,6,7,8,9,10]

for val in value:
    mysum = 0
    mysum += val
    pdb.set_trace()


print(mysum)


import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s', datefmt = '%m/%d/%y %I:%M%S %p')

logging.debug("This msg will be ignored")
logging.info("This should be logged")
logging.warning("And this will be logged too")


import timeit

print('by index', timeit.timeit(stmt="mydict['c']", setup="mydict = {'a':1,'b':2,'c':3}", number=1000000))
print('by get', timeit.timeit(stmt="mydict.get('c')", setup="mydict = {'a':1,'b':2,'c':3}", number=1000000))

def testme(this_dict, key):
    return this_dict[key]

print(timeit.timeit("testme(mydict,key)",setup="from __main__ import testme; mydict = {'a':1,'b':2,'c':3}; key = 'c'",number=10000))

import sys


def doubleit(x):
    if not isinstance(x, (int, float)):
        raise TypeError
    var = x * 2
    return var


def doublelines(filename):
    with open(filename) as fh:
        newlist = [str(doubleit(int(val))) for val in fh]
    with open(filename, 'w') as fh:
        fh.write('\n'.join(newlist))


if __name__ == '__main__':
    input_val = sys.argv[1]
    doubled_val = doubleit(input_val)

    print("The value of {} is {}".format(input_val, double_val))
