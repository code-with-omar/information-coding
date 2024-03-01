import string

message = "BAABABBBAABBBBAA"
dictionary = {}
# print(dictionary.keys())
tmp = ""
i = 1
last = 0
Flag = True
for x in message:
    tmp += x
    # print(tmp)
    Flag = False
    if tmp not in dictionary.keys():
        dictionary[tmp] = i
        tmp = ""
        i += 1
        Flag = True
if not Flag:
    last = dictionary[tmp]
res = []

for char, idx in dictionary.items():
    # print(char,idx) #first value,index
    tmp = ""
    s = ""
    for x, j in zip(char[:-1], range(len(char))):
        tmp += x  # x= alphabet j=frequency
        if tmp in dictionary.keys():
            take = dictionary[tmp]
            # print(take)
            s = str(take) + char[j + 1]
            # print(s)
    if len(char) == 1:
        s = char
    res.append(s)
    # print(res)
if last:
    res.append(string(last))
alphabet = string.ascii_uppercase
print(alphabet)

mark = dict(zip(alphabet, range(len(alphabet))))
print(mark)
final_res = []
for x in res:
    tmp = ""
    for char in x:
        if char.isalpha():
            print(char)      
            tmp += bin(mark[char])[2:]
            print(tmp)
        else:
            tmp += bin(int(char))[2:]
    final_res.append(tmp.zfill(4))

print(res)
print("Encoded: ", final_res)