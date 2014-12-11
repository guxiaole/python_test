# create a file

'makeTextfile.py --read and disply text file'

import os
ls=os.linesep

path='E:\STUDY\\'
#get filename
while True:
	fname=path+raw_input('input filename: ')
	if os.path.exists(fname):
		print "ERROR: '%s' already exists" % fname
	else:
		break

#get file context lines
all=[]
print "\n Enter lines ('.' by itself to quit).\n"

#loop untill user input
while True:
	entry=raw_input('>')
	if entry=='.':
		break
	else:
		all.append(entry)

#write lines to file
fobj=open(fname,'w')
fobj.writelines(['%s%s' %(x,ls) for x in all])
fobj.close()
print 'DONE!'
