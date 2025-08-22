library(tidyverse) # for tidy up the data

dt <- read.csv('columbus.csv')
View(dt)
names(dt) <- tolower(names(dt)) #to change name of columns from capital letter to small letter
View(dt)

# 2.2 Piping
# %>% pipe operator: it used to simplify the code and makes it more readable.
#library(tidyverse)
dt %>% head(5) # View fist five columns


dt %>%
  group_by(ew) %>%
  summarize(mean_crime = mean(crime, na.rm=T))
# A tibble: 2 x 2
#ew mean_crime
#<int>      <dbl>
#     0       303.
#    1       295.

selected_dt <- dt %>%
  select(neig, evi, al, crime)
View(selected_dt)

filtered_dt<-dt %>%
  filter(ew ==0) # only choose ew equal 0
View(filtered_dt)

filtered_dt1 <- dt %>%
  filter(ew==0 & open<2) # only choose ew equal 0 and open smaller than 2
View(filtered_dt1)

filtered_dt2<-dt %>%
  filter(ew==0 | open<2) # "&" and "|" mean both condition

selected_filtered_dt <- dt%>%
  select(neig, evi, al,ew,  crime)%>%
  filter(ew==1 & evi >0.3)
View(selected_filtered_dt)

#mutate() function used to add new variables
library(dplyr)
df <- tibble(x = c(1,3,5), y =c(2, 4, 6))
df %>% mutate(z = y / x)
df %>% mutate(z = x * y, .after = x)

df %>%
  select(x, y) %>%
  mutate(
    z = y * 2,
    z_squared = z * z
  )

dem_df2 %>%                  # 1. data
  group_by(citizen) %>%     #2. group by
  summarize(N = n()) 
# Reshaping
df_wide <- data.frame('ID'=c('a', 'b', 'c', 'd'),
                      'time1'=c(1:4),
                      'time2'=c(3,5,6,9))
df_wide
library(furniture)
df_long<-long(df_wide,
              c('time1', 'time2'),
              v.names='value')
df_long

df_wide<-wide(df_long,
              v.names=c('value'),
              timevar='time')
df_wide


