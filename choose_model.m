transports = readtable('data5.txt','Delimiter',' ','ReadVariableNames',true);
transports.gender = nominal(transports.gender);
modelspec = 'survival_days ~ age + donor_age + operation_year + gender + diagnosis';
mdl = fitlm(transports,modelspec)
plotResiduals(mdl)
mdl1 = step(mdl,'NSteps',10)
plotResiduals(mdl1)
coefnames = mdl1.CoefficientNames
mdl1.Formula
coefvals = mdl1.Coefficients(:,1); % table
coefvals = table2array(coefvals)