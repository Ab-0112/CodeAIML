# date formats
dat = as.Date('1970-01-04')
dat
as.numeric(dat)
# default format is yyyy-mm-dd 
as.Date('2010-10-15')
as.Date('11/15/2011', format = '%m/%d/%Y')
as.Date('11/10/2011', format = '%d/%m/%Y')
as.Date('11JUN22', format = '%d%b%y')
as.Date('11-DECEMBER-23', format = '%d-%B-%y')
dob = c('anil' = '2010-05-25', 'barath' = '1990-11-21',
        'chandran' = '1995-12-22','darshan'= '1990-11-20')
dob
DOB = as.Date(dob)
DOB
weekdays(DOB)   # day of the week
months(DOB)     # month born
quarters(DOB)   # which quarter
installed.packages()
install.packages('chron')
library(chron)
# date and time stored as one string
dt = "2012-09-19 08:45:20"
dt
# split them as date and time seperately
l = strsplit(dt, ' ')
l
class(l)
l[[1]][1]   # date component
l[[1]][2]   # time component
d1 = ISOdate(1987,5,15)
d2 = ISOdate(1997,5,15)
d2 - d1  # difference between two dates. diff in no. of days
# alternate time unit is desired use difftime()
# default units = 'days'
difftime(d2,d1)
difftime(d2,d1,units = 'days')
difftime(d2,d1,units = 'weeks')
difftime(d2,d1,units = 'hours')
# seq() to generate dates
da = seq(as.Date('1973-8-24'),by = 'days',length = 15)
da
# frequency table
tab = table(format(da,'%b'))
tab 
