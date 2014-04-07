def createtable():
	head=[]
	f=open('listProperties.txt','r')
	fw=open('table.txt','w')
	for line in f:
		head.append(line.strip())
		print >> fw, line.strip(),
	print >> fw
	f2=open('ISHLT.ttl','r')
	for line in f2:
		line=line.strip()
		if line:
			#store row
			line=line.split()
			if len(line)>3:
				d={}
			else:
				key=line[0].split(':')[1]
				start=line[1].find('"')
				end=line[1].rfind('"')
				value=line[1][start+1:end]
				d[key]=value
		else:
			#print row
			for a in head:
				if d.has_key(a):
					print >> fw, d[a],
				else:
					print >> fw, '-',
			print >> fw
			#d={}

if __name__=='__main__':
	createtable()
