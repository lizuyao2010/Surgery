# -*- coding: utf-8 -*-
import sparql
import os.path
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
import numpy as np
'''
def print_regression_line(var_x,var_y):
   x = np.array(var_x)
   y = np.array(var_y)
   n = np.max(x.shape)
   X = np.vstack([np.ones(n),x]).T
   w = np.linalg.lstsq(X,y)[0]
   count = 0
   for i in w:
      print "w["+str(count)+"]:" + str(i),
      count += 1
      if count == len(w):
         print
'''
def print_result(offset,f):
   endpoint='http://130.235.17.116:8000/openrdf-sesame/repositories/AAOT'
   statement=("""PREFIX aaot:<http://cs.lth.se/ontologies/aaot.owl#>
   	select * WHERE {
   	 ?name aaot:age ?age . 
   	 ?name aaot:age_donor ?age_donor . 
   	 ?name aaot:gender ?gen . 
            ?name aaot:survival_time ?survival_time .
            } limit 1000
            offset """
            +str(offset)
   	 )
   result = sparql.query(endpoint,statement)
   variables = result.variables
   for row in result.fetchall():
      values=sparql.unpack_row(row)
      i=1
      while i<len(values):
         if variables[i]=='gen':
            if values[i]=='F':
               values[i]=1
            else:
               values[i]=0
         print >> f,values[i],'\t',
         i+=1
      print >> f

if __name__=='__main__':
   offset=0
   if not (os.path.isfile('./data.txt')):
      f=open('data.txt','w')
      while offset<100000:
         print_result(offset,f)
         offset+=1000
   else:
      ages=[]
      survival_days=[]
      ages_donor=[]
      f=open('data.txt','r')
      for line in f:
         line=line.split()
         ages.append(line[0])
         ages_donor.append(line[1])
         survival_days.append(line[3])
      # One feature
      '''
      print_regression_line(ages, survival_days)
      print_regression_line(ages_donor, survival_days)
      # Multiple features
      print_regression_line([ages,ages_donor],survival_days)
'''
