interest = function(principal, rate, time, n) {
  if (principal > 0 && rate > 0 && time > 0) {
    interest1 = (principal * rate * time) / 100
    amount = principal * (1 + rate / (100 * n))^(n * time)
    interest2 = amount - principal
    print(paste("Simple Interest:", interest1), quote = FALSE)
    print(paste("Compound Interest:", interest2), quote = FALSE)
  } else {
    print("Principal, rate, and time must be greater than zero", quote = FALSE)
  }
}

interest(10000, 2.6, 2, 4)
