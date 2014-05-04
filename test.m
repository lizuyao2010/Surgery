people = readtable('test.txt','Delimiter',' ','ReadVariableNames',true);
mdl = stepwiselm(people,'constant','ResponseVar','height')