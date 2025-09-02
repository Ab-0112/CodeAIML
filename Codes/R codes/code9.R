#functions in r
naturalsum = function(n) {
  if (n <= 0) {
    return(0)
  } else {
    return(n + naturalsum(n - 1))
  }
}
num = as.numeric(readline("value:"))
result = naturalsum(num)
print(paste("sum of first",num,"numbers:",result)) 
