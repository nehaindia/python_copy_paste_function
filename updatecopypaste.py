#!/usr/bin/python2

import time,sys,os,os.path, shutil

cp=sys.argv[1:3]

src=cp[0]
dest=cp[1]

def cp(src,dest):
	sf=open(src,'r')
	df=open(dest,'w')
	for i in sf:
		df.writelines(i)
		print "file copies..Thanku"
		df.close()
		sf.close()
		return;

def qcp(src,dest):
		print "File already exists"
		ans=raw_input("do u want to overwrite ? y/n")
		if ans == 'n':
			print "ok..exiting.."
			exit()
		else:
			cp(src,dest)
			return;

if os.path.isdir(dest):
	print "Destination is Directory"
	#directory=os.path.dirname(dest)
	#print directory
	dest=os.path.join(dest,os.path.basename(src))
	if os.path.isfile(dest):
		qcp(src,dest)
		print "File into directory"
	else :
		cp(src,dest)
		

elif os.path.isfile(dest):
	qcp(src,dest)
			

else :
	cp(src,dest)
