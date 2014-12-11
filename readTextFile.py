# Read a file

'readTextFile.py --read and disply text file'

import os
ls=os.linesep
#path='E:\STUDY\\'
path =raw_input("input the path of file like this\n '>>C:\workpath'\n>>")

fname=path+raw_input('input the filename which you want: ')

#file to read
if os.path.exists(fname):
	fobj=open(fname,'r')
	for eachline in fobj:
		print eachline,
	fobj.close()
	#file=fobj.readlines(209715200)
	#print '%s%s' %(file,ls)
else:
	print "ERROR: '%s' not exists" % fname
