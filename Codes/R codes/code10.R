#dataframe 1
set.seed(120)
a = sample(1:1000,100)
b = sample(101:1000,100)
c = sample(201:1000,100)
d = sample(150:1000,100)
e = sample(701:1000,100)
df1 = data.frame(a,b,c,d,e)
head(df1)
summary(df1[c('c','e')])
df1[10:20,c('a','c','e')]
sortdf = df1[order(df1$b, decreasing = TRUE),]
head(sortdf)
newdf = df1[-(51:60),]
rownames(newdf) = NULL
head(newdf)
rownames(newdf)
tail(df)
