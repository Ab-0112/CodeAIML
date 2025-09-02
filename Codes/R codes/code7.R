# list operations
id = c(101,102,103)
name = c('santosh','sai','anuj')
mark = c(100,85,86)

# creation of a list
l = list(id,name,mark)
print(l)
class(l)
typeof(l)
is.list(l)

# named list
l1 = list(roll_no = id,name = name,mark1 = mark )
print(l1)
print(l1$roll_no)
print(l1[[1]])
print(l1$name)
print(l1[[2]])
print(l1$mark1)
print(l1[[3]])
print( l[[ 1 ]] )

# to extract individual element
print(l[[1]][1])
print(l[[2]][1])
l[[1]][1] 
l[[1]][1] = 1001

#deletion
l5 = l1[-1]
l5
l1
l6 = l1[c(-1,-3)]
l6
l1
mark = list(66,77,88)
l1 = append(l1,mark)
l1

#merge two lists
l1 = list(1:20)
l2 = list(21:40)
l3 = list(l1,l2)
l1
l2
l3
l3[[1]]
l3[[2]]
l3[[1]][1] 

# String functions
s = "String functions in R"
print(s)
typeof(s)
class(s)
tolower(s)
toupper(s)
substr(s,1,6)
substr(s,1,3)
substr(s,8,10)
gsub('R','java',s)
library(stringr)
s = str_replace(s,'R','java')
s
str_split(s,' ')
length(s)
nchar(s)
a = 'Welcome'
nchar(a)
a
b = casefold(a,upper = TRUE)
b
c = casefold(a,upper = FALSE)
c
d = tolower(b)
d
b
v = c("python","r","Java","JS")
v
nzchar(v)
v = c(v,"", "")
v
