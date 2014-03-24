import sparql
endpoint='http://130.235.17.116:8000/openrdf-workbench/repositories/AAOT/query'
statement=("""PREFIX aaot:<http://cs.lth.se/ontologies/aaot.owl#>
	select * WHERE {
	 ?id aaot:age ?age . 
	 ?id aaot:age_donor ?age_donor . 
	 ?id aaot:gender ?gen . }"""
	 )
result = sparql.query(endpoint,statement)
print result.variables
for row in result.fetchall():
   #print 'row:',row
   values=sparql.unpack_row(row)
   ID=values[0].split('#')[1]
   print ID, 'age:',values[1], 'age_donor:',values[2], 'gen:',values[3]
