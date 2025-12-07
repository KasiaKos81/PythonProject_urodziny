matrix =[[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

# to get i.e. no 9
print(matrix[2][2])

# to get i.e. no 6
print(matrix[1][2])

# to change no 6 into no 2100
matrix[1][2] = 2100

#  printig single value
print(matrix[1][2])
# printing entire new matrix
print(matrix)

text = "add,row,0,5"
print(type(text))

# how to split a long string
data = text.split(",")
print(data)