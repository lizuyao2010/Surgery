def findmost(d):
	max=['',0]
	for item in d.items():
		if item[1]>max[1]:
			max=list(item)
	return max[0]

def filltable(tableFile):
	context=open(tableFile,'r')
	i=1
	d={}
	head=[]
	for line in context:
		if i==1:
			line=line.strip().split()
			for col in range(0,len(line)):
				d[col]={}
				head.append(line[col])
		else:
			line=line.strip().split()
			j=0
			for col in line:
				if col=='-':
					None
				else:
					if not d[j].has_key(col):
						d[j][col]=1
					else:
						d[j][col]+=1
				j+=1		
		i+=1
        mostls=[]
	for key in d.keys():
		#find most
		most=findmost(d[key])
		mostls.append(most)
	for i in range(0,len(head)):
		print head[i],mostls[i]
if __name__=='__main__':
	filltable('newfilledtable.txt')
