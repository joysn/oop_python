import datetime
import abc

class WriteFile(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self,fname):
        self.fname = fname

    @abc.abstractmethod
    def write(self,text):
        return

    def write_line(self,fname,text):
        fh = open(self.fname, 'a')
        fh.write(text)
        fh.close()


class LogFile(WriteFile):

    def write(self,text):
        self.write_line(self.fname,datetime.datetime.now().strftime('%Y-%m-%d %H:%M')+'   '+text+'\n')

class DelimFile(WriteFile):

    def __init__(self,fname,delim):
        super(DelimFile,self).__init__(fname)
        self.delim = delim

    def write(self,my_list):
        self.write_line(self.fname,self.delim.join(my_list)+'\n')

