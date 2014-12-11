# Read a file

'readTextFile.py --read and disply text file'

import os
ls=os.linesep
#path='E:\STUDY\\'
path =raw_input("input the path of file and name like this\n '>>C:\workpath\ test.text'\n>>")

#fname=path+raw_input('input the filename which you want: ')

#file to readlines

try:
	fobj=open(fname,'r')
except IOError,e:
	print "file open failed:",e
else:
	for eachline in fobj:
		print eachline,
	fobj.close()

#if os.path.exists(fname):
	#fobj=open(fname,'r')
	#for eachline in fobj:
		#print eachline,
	#fobj.close()
	##file=fobj.readlines(209715200)
	##print '%s%s' %(file,ls)
#else:
	#print "ERROR: '%s' not exists" % fname
