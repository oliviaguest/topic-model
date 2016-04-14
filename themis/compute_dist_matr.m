pca_out = 0
corre = 0;
corre2 = 1;

dist_matr = zeros(size(data,2),size(data,2));

X1 = coeff(:,1);
Y1 = coeff(:,2);
for i = 1:size(data,2)
    for j = i+1:size(data,2)
        if pca_out
            dist_matr(i,j)=1/euclidean_distance([X1(i,:) Y1(i,:)],[X1(j,:) Y1(j,:)]);
            dist_matr(j,i)=1/euclidean_distance([X1(i,:) Y1(i,:)],[X1(j,:) Y1(j,:)]);
        elseif corre 
            dist_matr(i,j)=corr(coeff(i,:)',coeff(j,:)');        
            dist_matr(j,i)=corr(coeff(i,:)',coeff(j,:)');             
        elseif corre2 
            dist_matr(i,j)=corr(data(:,i),data(:,j));        
            dist_matr(j,i)=corr(data(:,i),data(:,j));  
        else
            dist_matr(i,j)=1/euclidean_distance(data(:,i),data(:,j));        
            dist_matr(j,i)=1/euclidean_distance(data(:,i),data(:,j));
        end
    end
end