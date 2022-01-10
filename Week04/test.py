from itertools import combinations

peoplelist = ["Lee ji-yeon", "Kim jeh-hyun", "Park hyeun-u", "Park hongjung", "Kim seul-gi", "Moon seung-hyeun", "Kim ji-hoon", "Kim joon-young", "Son ye-lim", "Sin min-soo"]
alreadyteam = set([(1, 6), (5, 7), (0, 9), (0, 2), (1, 3), (4, 6), (1, 2), (3, 6), (7, 9), (6, 8), (3, 9), (2, 6), (0, 4), (3, 8), (5, 9), (6, 9), (2, 4), (1, 8), (0, 6), (2, 5), (0, 1), (4, 5), (6, 7)])

posibleteam = set(combinations(range(10), 2)) - alreadyteam

counter_ = [0] * 10

for posibility in posibleteam:
    counter_[posibility[0]] += 1
    counter_[posibility[1]] += 1
    
    print(peoplelist[posibility[0]], peoplelist[posibility[1]])

print(counter_)