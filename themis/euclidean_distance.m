function [distance]=euclidean_distance(a,b)                      

distance=sqrt(sum((a-b).^2));