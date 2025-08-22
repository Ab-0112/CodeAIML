# How To Use R for Research
# 4- Importing data to R Programming

# Mainly researchers use .csv, .txt, .sav, and .xlxs format files.

# R base functions for importing data: read.table(), read.delim(), read.csv(), read.csv2()

# Download  used in this tutorial: https://github.com/Azad77/py4researchers/blob/main/data/columbus.csv  
#### Reading a local file

data <- read.csv("datasets/columbus.csv")
data
View(data) # to view data as table
# symbol in R used to write comment.

# For reading delimited tab separated file:
data1<- read.delim(file.choose())

# Read comma (",") separated values:
data2<-read.csv(file.choose()) # to choose file from directory

# Read semicolon (";") separated values:
data3 <- read.csv2(file.choose())

table<- read.table("datasets/columbus.csv", header=T, sep=";")
View(table)

delim = read.delim("D:/R4Researchers/columbus.csv", header=T, sep=";")
View(delim)

# Call function from libraries to read files:
library(readr)  # for read_csv
library(knitr)  # for kable
library(curl)

#### Reading an online file 
df <- read.table("https://s3.amazonaws.com/assets.datacamp.com/blog_assets/test.txt", header = FALSE)
df

df1 <- read.table("https://s3.amazonaws.com/assets.datacamp.com/blog_assets/test.csv", header = FALSE, sep = ",")
df1

df2 <- read.csv("https://s3.amazonaws.com/assets.datacamp.com/blog_assets/test.csv", header = FALSE)
df2

df3 <- read.csv2("https://s3.amazonaws.com/assets.datacamp.com/blog_assets/test.csv",  header= FALSE)
df3
