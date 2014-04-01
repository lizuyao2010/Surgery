#!/usr/bin/python

import sparql
import itertools

def read_list_attributes():
    list_attributes = []
    f = open('listProperties.txt', 'r')
    for line in f:
        list_attributes.append(line.strip())
    return list_attributes

def count_result_from_query(subset):
    value = 0;
    endpoint = 'http://130.235.17.116:8000/openrdf-sesame/repositories/AAOT'  
    statement_beginning = """PREFIX aaot:<http://cs.lth.se/ontologies/aaot.owl#>
   	select (count(*) as ?count) WHERE { \n"""
    statement_end = """ ?name aaot:survival_time ?survival_time .
            }"""
    statement_query = ""

    for i in subset:
        statement_query = statement_query + "?name aaot:"+i+" ?"+i+" .\n"

    statement = statement_beginning + statement_query + statement_end

    result = sparql.query(endpoint, statement)

    for row in result.fetchall():
        values = sparql.unpack_row(row)
        value = values[0]

    return value

def combinatorial_query():
    max_subset = []
    maxlen=0
    list_attributes = read_list_attributes()
    for L in range(len(list_attributes), 0, -1):
        for subset in itertools.combinations(list_attributes, L):
            value = count_result_from_query(subset)
            if ((value > 50000) and (len(subset) >= maxlen)):
                max_subset.append(list(subset))
                max=len(subset)
                print value,
                print subset
    return max_subset

if __name__ == "__main__":
    print combinatorial_query()
    
