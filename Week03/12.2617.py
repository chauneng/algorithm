import sys

N, M = map(int, sys.stdin.readline().split())

arr = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    arr[a][b] = 1


#두 노드 사이를 잇는 노드가 있다면 둘 사이의 대소비교가 가능하다. -> 플로이드 와샬의 응용
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if arr[i][k] and arr[k][j]:
                arr[i][j]=1

ans = 0

#각각의 구슬에 대해, 다른 구슬과 이어진 간선(크기 비교가 가능한 경우)이 N//2이상 있다면, 중간은 될 수 없다.
for i in range(1, N+1):
    left_cnt, right_cnt = 0, 0
    for j in range(1, N+1):
        if i == j:
            continue
        elif arr[i][j] == 1:
            right_cnt += 1
        #i보다 큰 j가 존재한다
        elif arr[j][i] == 1:
            left_cnt += 1
        #i보다 작은 j가 존재한다.
    if right_cnt > N//2 or left_cnt > N//2:
        ans += 1

print(ans)