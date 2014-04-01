#!/usr/bin/python
# -*- coding: utf-8 -*-

import sparql

def multiple_query():

    endpoint = 'http://130.235.17.116:8000/openrdf-sesame/repositories/AAOT'
    
    f_properties = open('listProperties.txt','r')
    
    statement_beginning = """PREFIX aaot:<http://cs.lth.se/ontologies/aaot.owl#>
   	select (count(*) as ?count) WHERE { \n"""
    
    statement_end = """ ?name aaot:survival_time ?survival_time .
            }"""

    offset = 0;
    max_list_attributes = []
    treshold = 10000
    line=f_properties.readlines()
    list_attributes = []
    for i in range(0, 1):
        list_attributes.append(line[i].strip())
        statement_query = ""
        statement_query = statement_query + "?name aaot:"+line[i].strip()+" ?"+line[i].strip()+" ."
        statement = statement_beginning + statement_query + statement_end +"\n"
        result = sparql.query(endpoint,statement)
        for row in result.fetchall():
            values = sparql.unpack_row(row)
            if (values[0] > treshold) and (len(list_attributes) > len(max_list_attributes)):
                max_list_attributes = list_attributes
                print str(values[0]), 
                print max_list_attributes
        for j in range(i+1, len(line)):
            latest_value = 0
            list_attributes.append(line[j].strip())
            statement_query = statement_query + "?name aaot:"+line[j].strip()+" ?"+line[j].strip()+" ."
            statement = statement_beginning + statement_query + statement_end+ "\n"
            result = sparql.query(endpoint,statement)
            for row in result.fetchall():
                values = sparql.unpack_row(row)
                latest_value = values[0]
                print values[0]
                if (values[0] <= treshold):
                    break
                if (values[0] > treshold) and (len(list_attributes) > len(max_list_attributes)):
                    max_list_attributes = list_attributes
                    print str(values[0]),
                    print max_list_attributes
            if(latest_value == 0):
                break

    return max_list_attributes

if __name__ == "__main__":
    multiple_query()

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
