close all
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

set(0,'DefaultLegendFontSize',8);
set(0,'DefaultAxesFontAngle','Normal');
set(0,'DefaultAxesFontWeight','Normal');
set(gcf,'color',[1 1 1])
set(gca,'color',[.75 .75 .75])


subplot(2,3,1)

data = data800
[coeff,score,latent,tsquared,explained,mu] = pca(data);
compute_dist_matr
imagesc(dist_matr);

YTickLabel = CDI_words;

%colorbar



title('800 topics (real)','FontSize',12)
grid on

subplot(2,3,2)

data = ((data800>0) -.5)*2;
[coeff,score,latent,tsquared,explained,mu] = pca(data);
compute_dist_matr
imagesc(dist_matr);

YTickLabel = CDI_words;

%colorbar



title('800 topics (-1,1)','FontSize',12)
grid on


subplot(2,3,3)

data = data800>0;
[coeff,score,latent,tsquared,explained,mu] = pca(data);
compute_dist_matr
imagesc(dist_matr);

YTickLabel = CDI_words;

%colorbar



title('800 topics (binary)','FontSize',12)
grid on

subplot(2,3,4)

data = data400;

[coeff,score,latent,tsquared,explained,mu] = pca(data);
compute_dist_matr
imagesc(dist_matr);
%colorbar


title('400 topics','FontSize',12)
grid on



subplot(2,3,5)
data = data200;
[coeff,score,latent,tsquared,explained,mu] = pca(data);
compute_dist_matr
imagesc(dist_matr);
%colorbar


title('200 topics','FontSize',12)
grid on



subplot(2,3,6)
data = data100;
[coeff,score,latent,tsquared,explained,mu] = pca(data);
compute_dist_matr
imagesc(dist_matr);
%colorbar


title('100 topics','FontSize',12)
grid on




