load data.txt;
x=data(:,[1,2]);
y=data(:,4);
b=regress(y,x)
yfit=x*b;

yresid = y - yfit;
SSresid = sum(yresid.^2);
SStotal = (length(y)-1) * var(y);
rsq = 1 - SSresid/SStotal