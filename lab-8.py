import math

matrix = [
    [1 / 8, 1 / 16, 1 / 32, 1 / 32],
    [1 / 16, 1 / 8, 1 / 32, 1 / 32],
    [1 / 16, 1 / 16, 1 / 16, 1 / 16],
    [1 / 4, 0, 0, 0],
]

# the marginal distribution of x

marginal_x = []
# print(len(matrix[0]))
for i in range(0, 4):
    sum_matrix = sum(matrix[j][i] for j in range(len(matrix)))
    marginal_x.append(sum_matrix)
# print(marginal_x)

# the marginal distribution of y

marginal_y = []
for i in range(len(matrix)):
    marginal_y.append(sum(matrix[i][j] for j in range(len(matrix[0]))))
# print(marginal_y)


def entropy(marginal_value):
    H = 0
    for x in marginal_value:
        if x == 0:
            continue
        H += -(x * math.log2(x))
    # print(H)
    return H


H_x = entropy(marginal_x)
print("Entropy Hx = ", H_x)
H_y = entropy(marginal_y)
print("Entropy Hy = ", H_y)

# conditional entropy
# H(x/y)
H_xy = 0
for i in range(len(matrix)):
    tmp = [(1 / marginal_y[i]) * matrix[i][j] for j in range(len(matrix[0]))]
    # print(tmp)
    tmp_en = entropy(tmp) * marginal_y[i]
    H_xy += tmp_en
# print(H_xy)

# H(Y/X)
H_yx = 0
for i in range(len(matrix[0])):
    tmp = [(1 / marginal_x[i]) * matrix[j][i] for j in range(len(matrix))]
    # print(tmp)
    tmp_en = entropy(tmp) * marginal_x[i]
    H_yx += tmp_en
# print(H_yx)
print("Conditional Entropy H(x|y): ", H_xy)
print("Conditional Entropy H(y|x): ", H_yx)

# Joint entropy
# H(x,y)
H_of_xy = H_x + H_yx
print("Joint Entropy H(x,y): ", H_of_xy)

# Mutual Information
# I(x,y)
I_of_xy = H_y - H_yx
print("Mutual Information: ", I_of_xy)
