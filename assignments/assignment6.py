import os


class ConfigKeyError(Exception):

    def __init__(self, this, key):
        self._key = key
        self._keys = this.keys()

    def __str__(self):
        return "Key \"{}\" not found. Availale Keys : {}".format(self._key, self._keys)


class ConfigDict(dict):

    def __init__(self, fname):
        self._fname = fname
        if not os.path.isfile(self._fname):
            try:
                open(self._fname, 'w').close()
            except IOError:
                raise IOError('must be valid file name')
        with open(self._fname) as fh:
            for line in fh:
                sp = line.rstrip().split('=', 1)
                dict.__setitem__(self, sp[0], sp[1])

    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)
        with open(self._fname, 'a') as fh:
            fh.write(key + '=' + value + '\n')

    def __getitem__(self, key):
        try:
            return dict.__getitem__(self, key)
        except:
            raise ConfigKeyError(self, key)

# try:
#    cd = ConfigDict('/a/b/doesnotexist.txt')
# except IOError:
#    print("IOError")
