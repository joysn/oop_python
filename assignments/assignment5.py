import os
import pickle

class ConfigKeyError(Exception):

    def __init__(self, this, key):
        self._key = key
        self._keys = this.keys()

    def __str__(self):
        return "Key \"{}\" not found. Available Keys : {}".format(self._key, self._keys)


class ConfigDict(dict):

    config_directory = '/oop_python/'

    def __init__(self, config_name):
        ConfigDict._fname = ConfigDict.config_directory+config_name+'.pickle'
        if not os.path.isfile(ConfigDict._fname):
            with open(self._fname,'wb') as fh:
                pickle.dump({'a':1},fh)

        with open(ConfigDict._fname,'rb') as fh2:
            unpickledlist = pickle.load(fh2)
            self.update(unpickledlist)

    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)
        with open(ConfigDict._fname, 'wb') as fh:
            pickle.dump(self, fh)


    def __getitem__(self, key):
        try:
            return dict.__getitem__(self,key)
        except:
            raise ConfigKeyError(self,key)


#cd = ConfigDict('/a/b/doesnotexist.txt')
#cc = ConfigDict('config_file.txt')
#print(cc['non_existing_key'])
