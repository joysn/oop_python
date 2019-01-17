import sys
from assignment3 import ConfigDict

cc = ConfigDict('config_file.txt')


if len(sys.argv) == 3:
    key = sys.argv[1]
    value = sys.argv[2]
    print('wrting data {} {}'.format(key,value))

    cc[key] = value
else:
    print('reading data')
    for key in cc.keys():
        print('    {} = {}'.format(key, cc[key]))

print(cc['sql_query'])
print(cc['email_to'])
cc['database'] = 'mysql_managed'
print(cc['database'])
