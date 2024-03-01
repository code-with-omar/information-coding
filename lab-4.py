# Let's say n = 8, which is a power of 2 (2^3 = 8).
# n - 1 will be 7 (binary representation: 0111).
# Performing the bitwise AND operation: 8 & 7, we get 0000, which is 0.
# So, 8 satisfies the condition, indicating it's a power of 2.
# In summary, if n & (n - 1) == 0: checks whether n is a power of 2. If the condition is true, then n is a power of 2; otherwise, it's not.
def isPowerOfTwo(n):
    if n == 0:
        return False
    if n & (n - 1) == 0:
        return True


inp = input("Enter Input(hamming Code): ")
hamming = ""
length = len(inp)

# calculate redundant bits
r = 0
for i in range(length):
    if 2**i == length + i + 1:
        r = i

        break

# hamming code with parity positioned
k = 0
for i in range(1, length + r + 1):
    if isPowerOfTwo(i):
        hamming += "p"
    else:
        hamming += inp[k]
        k += 1

print("Position generate parity bit : ", hamming)

# calculate parity bits
res = 0
for i in range(len(hamming)):
    if hamming[i] == "1":
        res ^= i + 1

P = bin(res)[2:].zfill(r)[::-1]

# hamming code generate
k = 0
hamming_list = list(hamming)
for i in range(len(hamming)):
    if hamming_list[i] == "p":
        hamming_list[i] = P[k]
        k += 1
hamming = "".join(hamming_list)
print("Hamming code : ", hamming)

# Error  detection
rcv = input("Enter Received Code: ")
res = 0
for i in range(len(rcv)):
    if rcv[i] == "1":
        res ^= i + 1

if res == 0:
    print("No Error")
else:
    print("Error at : ", res)
