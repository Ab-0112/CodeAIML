loops = function() {
  print("for loop")
  for (i in 1:5) {
    print(i)
  }
  
  print("while loop")
  i = 1
  while (i <= 5) {
    print(i)
    i = i + 1
  }
  
  print("repeat loop")
  i = 1
  repeat {
    print(i)
    i = i + 1
    if (i == 5) {
      break
    }
  }
}

loops()