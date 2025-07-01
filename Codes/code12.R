# data visualization
library(datasets)
# box plot
attach(iris)
par(mfrow=c(2,2))
boxplot(iris$sl, col="green", main="Sepal length",notch = TRUE)
boxplot(iris$pl, col="yellow",breaks = 25, main="Petal length",notch = TRUE)
boxplot(iris$sw, col="darkgreen",breaks = 50, main="Sepal width",notch = TRUE)
boxplot(iris$pw, col="pink",breaks = 75, main="Petal width",notch = TRUE)

# histogram
attach(iris)
par(mfrow=c(2,2))
with(iris, hist(iris$sw, main=" Sepal width",col="green"))
with(iris, hist(iris$pw, main="Petal width",col="darkblue"))
with(iris, hist(iris$pl, main="Petal length",col="pink"))
with(iris, hist(iris$pl, main=" Petal length",col="orange"))

# scatter plot
attach(iris)
par(mfrow=c(2,2))
with(iris, plot(x = iris$sl, y = iris$sw, main="Sepal length and Sepal width",col="green",pch = 19))
with(iris, plot(x = iris$pl, y = iris$pw, main="Petal length and Sepal length",col="darkblue",pch = 10))
with(iris, plot(x = iris$sl, y = iris$pl, main="Sepal width and Petal width",col="pink",pch = 11))
with(iris, plot(x = iris$sw, y = iris$pw, main="petal length and Petal width",col="orange",pch = 12))

# violin plot
library('vioplot')
attach(iris)
par(mfrow=c(2,2))
with(iris, vioplot(iris$sw, main=" Sepal width",col="green"))
with(iris, vioplot(iris$pw, main="Petal width",col="darkblue"))
with(iris, vioplot(iris$pl, main="Petal length",col="pink"))
with(iris, vioplot(iris$pl, main=" Petal length",col="orange"))

# bar plot
barplot(table(iris$class),col = c("orange1", "chocolate", "coral"))
