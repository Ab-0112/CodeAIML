# Create a 2x3 array
arr <- array(1:6, dim = c(2, 3))
print(arr)

# Create a 3x3x2 array
arr3d <- array(1:18, dim = c(3, 3, 2))
print(arr3d)

# Accessing elements in a 2D array
print(arr[1, 2])  # Element in first row, second column
print(arr[, 2])   # Entire second column
print(arr[1, ])   # Entire first row

# Accessing elements in a 3D array
print(arr3d[1, 2, 1])  # Element in first matrix, first row, second column

# Modify an element
arr[1, 2] <- 10
print(arr)

# Arithmetic operations
arr1 <- array(1:6, dim = c(2, 3))
arr2 <- array(7:12, dim = c(2, 3))

# Element-wise addition
sum_arr <- arr1 + arr2
print(sum_arr)

# Element-wise multiplication
prod_arr <- arr1 * arr2
print(prod_arr)

# Apply a function to array margins
# Calculate the sum for each row
row_sums <- apply(arr, 1, sum)
print(row_sums)

# Calculate the sum for each column
col_sums <- apply(arr, 2, sum)
print(col_sums)
