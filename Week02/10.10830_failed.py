from sys import stdin

n , b = map(int, stdin.readline().split())

a = [list(map(int, stdin.readline().split())) for _ in range(n)]

# print(a)

def transform(originalList: list) -> list:
    transList = []
    for i in range(n):
        tmpList = []
        for j in range(n):
            tmpList.append(originalList[j][i])
        transList.append(tmpList)
    return transList

# print(transform(a))

def calculate(originalList: list, transList: list) -> list:
    calculatedList= []
    for i in range(n):
        tmpList = []
        for j in range(n):
            tmpNum = 0
            for k in range(n):
                tmpNum += originalList[j][k]*transList[j][k]
            tmpList.append(tmpNum)
        calculatedList.append(tmpList)

    return calculatedList

print(calculate(a, transform(a)))