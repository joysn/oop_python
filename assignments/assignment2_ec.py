import datetime

class WriteFile(object):

    def __init__(self,fname,type):
        self.fname = fname
        self.type=type()
        self.fh = open(self.fname, 'a')

    def write(self,text):
        formatted_text = self.type.format_text(text)
        self.fh.write(formatted_text)

    def close(self):
        self.fh.close()


class LogFormatter(object):

    def format_text(self,text):
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M')+'   '+text+'\n'

class CSVFormatter(object):

    def __init__(self):
        self.delim = ','

    def format_text(self,text):
        for i in range(0,len(text)):
            if self.delim in text[i]:
                text[i] = "\""+text[i]+"\""
        return self.delim.join(text)+'\n'

