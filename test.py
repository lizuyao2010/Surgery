# -*- coding: utf-8 -*-
import sparql
endpoint='http://130.235.17.116:8000/openrdf-workbench/repositories/AAOT/query'
statement=("""PREFIX aaot:<http://cs.lth.se/ontologies/aaot.owl#>
	select * WHERE {
         ?name aaot:transplant_id ?transplant_id .
	 ?name aaot:age ?age . 
	 ?name aaot:age_donor ?age_donor . 
	 ?name aaot:gender ?gen . 
         ?name aaot:survival_time ?survival_time .
         }"""
	 )
result = sparql.query(endpoint,statement)
variables = result.variables
for row in result.fetchall():
   values=sparql.unpack_row(row)
   i=1
   while i<len(values):
      print variables[i],values[i],'\t',
      i+=1
   print 
