close all
cdi_word_list
lsi_cec_400topics
lsi_cec_200topics
lsi_cec_100topics
lsi_cec_50topics

set(0,'DefaultAxesFontName','Ayuthaya');
set(0,'DefaultAxesFontSize',8);
set(0,'DefaultAxesXcolor',[.5 .5 .5]);
set(0,'DefaultAxesYcolor',[.5 .5 .5]);

set(0,'DefaultLegendFontSize',8);
set(0,'DefaultAxesFontAngle','Normal');
set(0,'DefaultAxesFontWeight','Normal');
set(gcf,'color',[1 1 1])
set(gca,'color',[.75 .75 .75])

data = data800;


subplot(2,2,1)

plot(data800)
xlabel(['topic index']) 
ylabel(['weight']) 

title('word representations acorss 800 topics','FontSize',12)
grid on


subplot(2,2,2)

plot(data400)
xlabel(['topic index']) 
ylabel(['weight']) 

title('word representations acorss 400 topics','FontSize',12)
grid on


subplot(2,2,3)

plot(data200)
xlabel(['topic index']) 
ylabel(['weight']) 

title('word representations acorss 200 topics','FontSize',12)
grid on


subplot(2,2,4)

plot(data100)
xlabel(['topic index']) 
ylabel(['weight']) 

title('word representations acorss 100 topics','FontSize',12)
grid on

