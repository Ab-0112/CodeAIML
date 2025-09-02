#vector operations
vecop = function()
{
  vec = c(1, 2, 3, 4, 5)  
  print(vec + 2)
  print(vec * 3) 
  vec1 = c(1, 2, 3)
  vec2 = c(4, 5, 6)
  print(vec1 + vec2)  
  print(vec1 * vec2)  
  print(vec[1])  
  print(vec[2:4])  
  print(vec[c(1, 3, 5)])  
  print(vec[vec==3])  
  print(vec[vec %% 2 == 0])  
}
vecop()
