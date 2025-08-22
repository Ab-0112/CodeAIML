# How To Use R for Research
# 5- Exporting data from R programming
#### Create data:
data <- c(1977, 1979, 2013, 2014,'', 2015)

#### Save data as "csv" format comma separated:
write.csv(data, 'created_data.csv') 

#### Save as semicolon(;) separated csv file:
write.csv2(data, file='data_semicolon.csv')

#### Save data as txt file:
write.table(data, file= 'data.txt', sep = '\t', row.names=T) # \t is tab

#### Compressing and saving files:
write.csv(data, file = bzfile('data_ziped.csv.bz2'))

#### Save as RData:
# If we have a, b, c, d, and e objects we can save them as RData then reload it in the new session

a<- c(5)
b<- c(-1)
c<- c(15)
d<- c(55)
e<- c('NA')
save(a, b, c, d, e, file='test.RData') # Rdata is used to save multiple R objects
load('C:\\Users\\Azad\\Documents\\test.RData')

#### Save an object to rds file:
saveRDS(data, 'firstData.rds') # Rds is used to save a single R object

# Restore it
rds_data <- readRDS("firstData.rds") 

#### Save workspace: 
# The workspace is your current R working environment and includes any user-defined objects (vectors, matrices, data frames, lists, functions).
save.image(file='workspace_2021.RData')
load('workspace_2021.RData')


