

[num1] = xlsread('LSI800topics.xls',1);
[num2] = xlsread('LSI800topicsB.xls',1);

data800 = [num1(2:end,:) num2];
