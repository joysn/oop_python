import sys
from assignment5 import ConfigDict

cc = ConfigDict('pickle_config_file')

cc['newkey10'] = 'newvalue1'
cc['newkey20'] = 'newvalue2'
for key in cc.keys():
    print('    {} = {}'.format(key,cc[key]))

"""
if len(sys.argv) == 3:
    key = sys.argv[1]
    value = sys.argv[2]
    print('wrting data {} {}'.format(key,value))

    cc[key] = value
else:
    print('reading data')
    for key in cc.keys():
        print('    {} = {}'.format(key, cc[key]))

"""
"""
#print(cc['newkey1'])
#cc['database'] = 'mysql_managed'#
#print(cc['database'])
