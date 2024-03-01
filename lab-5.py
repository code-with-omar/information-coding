import math

# given matrix
matrix = [[2 / 3, 1 / 3], [1 / 3, 2 / 3]]
print("Symmetric matrix is : ")
for i in range(len(matrix)):
    for j in range(len(matrix)):
        print("%.2f " % matrix[i][j], end=" ")
    print()
# calculate H(Y/X) using formula (1-p)log(1/1-p)+plog(1/p)
Hp = matrix[0][0] * math.log2(1.0 / matrix[0][0]) + matrix[0][1] * math.log2(
    1.0 / matrix[0][1]
)
print("Conditional probability H(Y/X) = %.3f" % Hp, "bits/mgx symbol")

# now calculate channel capacity using formula C=1-H(Y/X)
C = 1 - Hp
print("Channel Capacity is = %.3f" % C, "bits/msg symbol")
