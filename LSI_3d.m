
cdi_word_list
lsi_cec_800topics
lsi_cec_400topics
lsi_cec_200topics
lsi_cec_100topics
lsi_cec_50topics

set(0,'DefaultAxesFontName','Ayuthaya');
set(0,'DefaultAxesFontSize',8);
set(0,'DefaultAxesXcolor',[.5 .5 .5]);
set(0,'DefaultAxesYcolor',[.5 .5 .5]);
set(0,'DefaultAxesZcolor',[.5 .5 .5]);

set(0,'DefaultLegendFontSize',8);
set(0,'DefaultAxesFontAngle','Normal');
set(0,'DefaultAxesFontWeight','Normal');
set(gcf,'color',[1 1 1])
set(gca,'color',[.75 .75 .75])

data = (data800);
[coeff,score,latent,tsquared,explained,mu] = pca(data);


subplot(2,2,1)


X1 = coeff(:,1);
Y1 = coeff(:,2);
Z1 = coeff(:,3);

axis([min(X1) max(X1) min(Y1) max(Y1) min(Z1) max(Z1)])


plot3(X1,Y1,Z1,'sr','MarkerSize',1,'LineWidth',12)  
for ii = 1:size(X1,1)   
    text(X1(ii,1), Y1(ii,1), Z1(ii,1), [cellstr(CDI_words(ii))])
end



xlabel(['1st cmpnt (' int2str(round(10*explained(1))/10) '%)']) 
ylabel(['2nd cmpnt (' int2str(round(10*explained(2))/10) '%)']) 
zlabel(['3rd cmpnt (' int2str(round(10*explained(3))/10) '%)']) 

title('wikipedia, 800 topics','FontSize',12)
%axis([min(X1)-0.01 max(X1)+0.01 min(Y1)-0.01 max(Y1)+0.01])
grid on



subplot(2,2,2)
data = data400;
[coeff,score,latent,tsquared,explained,mu] = pca(data);


X1 = coeff(:,1);
Y1 = coeff(:,2);
Z1 = coeff(:,3);

axis([min(X1) max(X1) min(Y1) max(Y1) min(Z1) max(Z1)])


plot3(X1,Y1,Z1,'sr','MarkerSize',1,'LineWidth',12)  
for ii = 1:size(X1,1)   
    text(X1(ii,1), Y1(ii,1), Z1(ii,1), [cellstr(CDI_words(ii))])
end



xlabel(['1st cmpnt (' int2str(round(10*explained(1))/10) '%)']) 
ylabel(['2nd cmpnt (' int2str(round(10*explained(2))/10) '%)']) 
zlabel(['3rd cmpnt (' int2str(round(10*explained(3))/10) '%)']) 

title('wikipedia, 400 topics','FontSize',12)
%axis([min(X1)-0.01 max(X1)+0.01 min(Y1)-0.01 max(Y1)+0.01])
grid on



subplot(2,2,3)
data = data200;
[coeff,score,latent,tsquared,explained,mu] = pca(data);

X1 = coeff(:,1);
Y1 = coeff(:,2);
Z1 = coeff(:,3);

axis([min(X1) max(X1) min(Y1) max(Y1) min(Z1) max(Z1)])


plot3(X1,Y1,Z1,'sr','MarkerSize',1,'LineWidth',12)  
for ii = 1:size(X1,1)   
    text(X1(ii,1), Y1(ii,1), Z1(ii,1), [cellstr(CDI_words(ii))])
end


xlabel(['1st cmpnt (' int2str(round(10*explained(1))/10) '%)']) 
ylabel(['2nd cmpnt (' int2str(round(10*explained(2))/10) '%)']) 
zlabel(['3rd cmpnt (' int2str(round(10*explained(3))/10) '%)']) 

title('wikipedia, 200 topics','FontSize',12)
%axis([min(X1)-0.01 max(X1)+0.01 min(Y1)-0.01 max(Y1)+0.01])
grid on



subplot(2,2,4)
data = data100;
[coeff,score,latent,tsquared,explained,mu] = pca(data);


X1 = coeff(:,1);
Y1 = coeff(:,2);
Z1 = coeff(:,3);

axis([min(X1) max(X1) min(Y1) max(Y1) min(Z1) max(Z1)])


plot3(X1,Y1,Z1,'sr','MarkerSize',1,'LineWidth',12)  
for ii = 1:size(X1,1)   
    text(X1(ii,1), Y1(ii,1), Z1(ii,1), [cellstr(CDI_words(ii))])
end


xlabel(['1st cmpnt (' int2str(round(10*explained(1))/10) '%)']) 
ylabel(['2nd cmpnt (' int2str(round(10*explained(2))/10) '%)']) 
zlabel(['3rd cmpnt (' int2str(round(10*explained(3))/10) '%)']) 

title('wikipedia, 100 topics','FontSize',12)
%axis([min(X1)-0.01 max(X1)+0.01 min(Y1)-0.01 max(Y1)+0.01])
grid on


