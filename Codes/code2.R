#conditional statements
print_factors = function(n){
  if (n>0){
    for (i in 1:n) {
      if (n %% i == 0) {
        cat(i," ")
      }
    }
  }else if(n == 0){
    print("Zero . no Factors",quote = FALSE)
  }else{
    print("Input No is -ve",quote = FALSE)
  } }
print_factors(200)
