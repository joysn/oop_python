from assignment2_ec import WriteFile, LogFormatter,CSVFormatter

writelog = WriteFile('log2.txt',LogFormatter)
writecsv = WriteFile('text2.csv',CSVFormatter)

writecsv.write(['a','b,2','c','d'])
writelog.write('this is a log message')

writecsv.write(['1','2','3','4'])
writelog.write('this is another log message')

writecsv.close()
writelog.close()
