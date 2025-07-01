#matrix operations
set.seed(100)
samp1 =sample(100:300,30)
mat1 = matrix(samp1,ncol=5,byrow=TRUE)
mat1
mat1[1:3,c(-1,-2,-3)]
mat1[c(2,4,5),c(1,3,5)]
sum(mat1[,1])
apply(mat1,1,max)
apply(mat1,1,sd)
apply(mat1,1,var)
apply(mat1,2,sd)
apply(mat1,2,var)
apply(mat1,1,mean)
rowSums(mat1)
colSums(mat1)
