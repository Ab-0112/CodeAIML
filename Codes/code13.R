# data visualization 2
library(lattice)
library(datasets)
# take a copy
df = mtcars
dim(df)
head(df,10)
str(df)
# to know data type of each column in  df
sapply(df, class)
# summary statistics
summary(df)
# pre-processing
# check for missing values
is.na(df)
miss = colSums(is.na(df))
miss  # there are no missing values
# check unique values of gear
unique(df$gear)
# sort the unique values
sort(unique(df$gear))
# though the gear variable is integer, 
# it has only three values. ie discrete values.
# Hence, convert it to factor variable with 3 labels.
# since some machine learning models expects the same.
df$gear = as.factor(as.integer(df$gear))
# check cylinder
unique(df$cyl) 
# convert to factor
df$cyl = as.factor(as.integer(df$cyl))
# check am
unique(df$am)
# convert to factor
df$am = as.factor(as.integer(df$am))
unique(df$vs)
# convert to factor
df$vs = as.factor(as.integer(df$vs))
unique(df$carb)
# convert to factor
df$carb = as.factor(as.integer(df$carb))
# check the total number of unique values for each column
# change the column name each time.
# to decide for conversion as factor
names(df)    # all column names
length(unique(df$vs))
# check data types of df
sapply(df, class)
# summary statistics
summary(df)
# histogram
# syntax barchart(formula, data = dataframe)
# single attribute
histogram(~mpg, data = df)
histogram(~wt, data = df)
# box plot
# plot a single attribute
bwplot(~ mpg | gear, data = df)
bwplot(~ mpg |cyl, data = df)
bwplot(~ mpg, data = df)
# plot two attributes
# scatter plot
xyplot(wt ~ mpg, data = df)
# density plot
densityplot(~ hp, data = df)
densityplot(~ mpg, data = df)
densityplot(~ disp, data = df)

