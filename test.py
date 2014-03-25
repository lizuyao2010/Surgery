# -*- coding: utf-8 -*-
import sparql
import os.path

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
      print "nothing"