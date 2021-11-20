from itertools import combinations, permutations
from sys import stdin

numOfCities = int(stdin.readline())
expenses = []
cities = []

for i in range(numOfCities):
    expenses.append(list(map(int, stdin.readline().split())))
    cities.append(i)

minimum = 1000001

def searchForRoutes(i: int):
    global minimum
    totalExpense = 0
    # print(i)
    if i == len(cities):
        return
    else:
        cities.append(i)
        # print(cities)
        routes = combinations(permutations(cities,2),numOfCities+1)
        # totalExpense = 0
        for j in routes:                #순회 루트 중 한 개를 선택한다
            for k in j:                 #길을 선택한다
                r=k[0]
                c=k[1]
                if expenses[r][c] == 0: #비용이 0이면 순회가 불가능하다는 뜻이므로 초기화한다
                    totalExpense = 0
                    break
                else:
                    totalExpense += expenses[r][c]
                    # print(totalExpense)
            if 0 < totalExpense < minimum:
                minimum = totalExpense  
        cities.remove(i)
        print(minimum)
        searchForRoutes(i+1)
        return

searchForRoutes(0)
print(minimum)