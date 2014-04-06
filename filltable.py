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
	for row in table:
		for col in row:
			if table[row][col]=='-':
				table[row][col]=mostls[col]
			print table[row][col],

	return table
if __name__=='__main__':
	table = filltable('table.txt')