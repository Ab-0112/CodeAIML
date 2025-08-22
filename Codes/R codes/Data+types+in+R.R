# Numeric
a <- c(-1, -3, 0, 5, 7, 8, 4, 6.3, 10)
a
typeof(a)
# Factor
drink_vector <- c('milk', 'water', 'juice')
drink_factor <- factor(drink_vector)
drink_factor
# Character
d <- c('Hellow world', 'R is fun!')
d
# Create a dataframe
a <- c(1, 3, 5, 7)
b <- c(2, 4, 6, 8)
df <- data.frame(a, b)

# Add a column with the $ operator
df$new_column <- c(1, 2, 3, 4)
View(df)
# Add a column with the cbind function
df <- cbind(df, new_new_column = c('a', 'b', 'c', 'd'))

# View the dataframe as a table in RStudio
View(df)

# Get the names of the dataframe
names(df)

# Display the structure of the dataframe
str(df)

# Summary
summary(df)
