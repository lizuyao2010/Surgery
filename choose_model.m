transports = readtable('~/Downloads/newfilledtable.txt','Delimiter',' ','ReadVariableNames',true);
%{
transports.gender = nominal(transports.gender);
transports.ABO = nominal(transports.ABO);
transports.ABO_donor = nominal(transports.ABO_donor);
%}
modelspec = 'survival_time ~ 1 + age + age_donor + operation_year + gender + diagnosis';
%modelspec = 'survival_time ~ diagnosis + age + gender + height + weight + history_cigarette + COPD + history_diabetes + history_peptic_ulcer + history_hypertension + history_perip_vasc + history_cereb_vasc + history_cereb_vasc_event + history_dialysis + infection_iv_therapy + cytomegalovirus_igg + antiarrythmics + amiodarone + implantable_defibrillator + history_angina + PRA + history_transfusion + history_transplant + history_card_surg + history_malignancy + oxygen_exercise + functional_status + working_income + hemo_pcw + hemo_co + hemo_pa_sys + creatinine + serum_bilirubin + serum_albumin + medical_condition + inotropic_support + mechanical_ventilator + ballon_pump + ECMO + ventricular_assist + age_donor + gender_donor + height_donor + weight_donor + history_cigarette_donor + history_alcohol_donor + history_cocaine_donor + history_diabetes_donor + history_hypertension_donor + LVEF_donor + cytomegalovirus_donor + creatinine_donor + BUN_donor + serum_bilirubin_donor + ischemic_time_donor + cause_of_death_donor + a1 + a2 + b1 + b2 + dr1 + dr2 + a1_donor + a2_donor + b1_donor + b2_donor + dr1_donor + dr2_donor + ABO + ABO_donor + operation_year + status';
%mdl = fitlm(transports,modelspec)
mdl=stepwiselm(transports,'constant','ResponseVar','survival_time','PredictorVars',{'age','age_donor','operation_year','gender','diagnosis'},'CategoricalVar',{'gender'});
%{
plotResiduals(mdl)
mdl1 = step(mdl,'NSteps',10)
plotResiduals(mdl1)
coefnames = mdl1.CoefficientNames
mdl1.Formula
coefvals = mdl1.Coefficients(:,1); % table
coefvals = table2array(coefvals)
%}