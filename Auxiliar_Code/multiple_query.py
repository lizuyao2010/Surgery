#!/usr/bin/python
# -*- coding: utf-8 -*-

f_properties = open('listProperties.txt','r')
f_test_query = open('testQuery.txt','w')

statement_beginning = """PREFIX aaot:<http://cs.lth.se/ontologies/aaot.owl#>
   	select (count(*) as ?count) WHERE { \n"""

statement_end = """ ?name aaot:survival_time ?survival_time .
            } limit 1000
            offset """

offset = 1000;

line=f_properties.readlines()
for i in range(0, len(line)):
    statement_query = ""
    statement_query = statement_query + "?name aaot:"+line[i]+" ?"+line[i]+" .\n"
    statement = statement_beginning + statement_query + statement_end + str(offset) + "\n"
    f_test_query.write(statement)
    for j in range(i+1, len(line)):
        statement_query = statement_query + "?name aaot:"+line[j]+" ?"+line[j]+" ."
        statement = statement_beginning + statement_query + statement_end + str(offset) + "\n"
        f_test_query.write(statement)

'''
Show: 

select (count(*) as ?count)
where {
?name aaot:transplant_id ?id .
?name aaot:survival_time ?survival_time .
}

Show:

select * 
where {
?name aaot:transplant_id ?id .
?name aaot:survival_time ?survival_time .
}
'''
        
                     

