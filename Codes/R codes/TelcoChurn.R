# Importing the libraries
library(tidyverse)
library(caret)
library(readr)
Telco_Customer_Churn <- read_csv("datasets/Telco-Customer-Churn.csv")
head(Telco_Customer_Churn,n = 5)
Telco_Customer_Churn.is