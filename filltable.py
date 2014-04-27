import random
def findmost(d):
	max=['',0]
	for item in d.items():
		if item[1]>max[1]:
			max=list(item)
	if max[0]=='-':
		max[0]=random.choice(d.keys())
	return max[0]

def filltable(tableFile):
	context=open(tableFile,'r')
	i=1
	d={}
	table=[]
	for line in context:
		if i==1:
			line=line.strip().split()
			for col in range(0,len(line)):
				d[col]={}
		else:
			row=[]
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
				row.append(col)
				j+=1
			table.append(row)
		i+=1
        mostls=[]
	for key in d.keys():
		#find most
		most=findmost(d[key])
		mostls.append(most)
	i=0
	for row in table:
		j=0
		for col in row:
			if j==0:
				j+=1
				continue
			if col=='-':
				table[i][j]=mostls[j]
			print table[i][j],
			j+=1
		print
		i+=1
	return table
if __name__=='__main__':
	table = filltable('table.txt')
