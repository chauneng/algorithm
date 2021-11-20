import sys, heapq

n = int(sys.stdin.readline().strip())
card_deck = []
answer = 0

for _ in range(n):
    heapq.heappush(card_deck, int(sys.stdin.readline().strip()))


if n == 1:
    answer = card_deck[0]

else:
    while len(card_deck) > 1: #1개일 경우 비교하지 않아도 된다
        temp_1 = heapq.heappop(card_deck) #제일 작은 덱
        temp_2 = heapq.heappop(card_deck) #두번째로 작은 덱
        answer += temp_1 + temp_2 #현재 비교 횟수를 더해줌
        heapq.heappush(card_deck, temp_1 + temp_2) #더한 덱을 다시 넣어줌
    
print(answer)
