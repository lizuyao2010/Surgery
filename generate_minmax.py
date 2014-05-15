f=open('mostfrequent.txt','r')
for line in f:
	line=line.strip().split()
	print "fprintf(\'"+line[0]+": %d\\n\',"+"max(transports."+line[0]+"));"