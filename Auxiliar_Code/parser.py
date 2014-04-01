#!/usr/bin/python

import os.path

f=open('../../Project_EDAN50/properties.ttl','r')
f2=open('listProperties.txt','w')

for line in f:
    if not "@prefix" in line:
        line = line.split()
        if line:
            line = line[0].split(':')
            if not '' in line:
                if 'id' in line:
                    f2.write('transplant_id\n')
                    f2.write('patient_id\n')
                else:
                    f2.write(line[1]+"\n")

f2.close()
f.close()
