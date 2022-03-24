participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

answer = ''
temp = 0
dic = {}
for part in participant:
    dic[hash(part)] = part
    temp += hash(part)
    print(dic)
    print(temp)
for com in completion:
    temp -= hash(com)
    print(dic)
    print(temp)
answer = dic[temp]

print(answer)