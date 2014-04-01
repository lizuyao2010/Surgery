#!/usr/bin/python
# -*- coding: utf-8 -*-
import sparql
import os.path

def print_result(attributes,offset,f):
   endpoint='http://130.235.17.116:8000/openrdf-sesame/repositories/AAOT'
   statement_beginning="""PREFIX aaot:<http://cs.lth.se/ontologies/aaot.owl#>
   	select * WHERE { """
              
   statement_ending=""" ?name aaot:survival_time ?survival_time .
            } limit 1000
            offset"""

   statement_query = ""
   for i in attributes:
      statement_query = statement_query + "?name aaot:"+i+" ?"+i+" ."

   statement = (statement_beginning + statement_query + statement_ending + str(offset))

   result = sparql.query(endpoint,statement)
   variables = result.variables
   for row in result.fetchall():
      values=sparql.unpack_row(row)
      i=1
      while i<len(values):
         print >> f,values[i],'\t',
         i+=1
      print >> f

if __name__=='__main__':
   offset=0
   fd_properties=open('listProperties.txt','r')
   for line in fd_properties:
      print line,   
   attributes = raw_input('Select your attributes(separated by space): ');
   
   list_attributes = attributes.split()
   if not (os.path.isfile('./data_'+attributes+'.txt')):
      f=open('data_'+attributes+'.txt','w')
      f.write(attributes+"\tSurvival_days"+"\n")
      while offset<100000:
         print_result(list_attributes,offset,f)
         offset+=1000

