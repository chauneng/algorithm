# #행렬 곱셈 함수
# def matrix_mul(a, b):
#     result = [[0]* N for _ in range(N)]
#     for i in range(N):
#         for j in range(N):
#             for k in range(N):
#                 result[i][j] += a[i][k] * b[k][j]
    
#     for i in range(N):
#         for j in range(N):
#             result[i][j] %= 1000
                
#     return result
    
    
# #2진법으로 변환하여 분할정복 실행
# N, B = map(int, input().split())
# matrix = [list(map(int, input().split())) for _ in range(N)]
# B = bin(B)[2:] #2진법으로 변환

# #단위 행렬
# identity_matrix = [[1 if i == j else 0 for i in range(N)] for j in range(N)]

# #2진법 자릿수 만큼 제곱 & 제곱한 행렬 끼리 곱해줌
# result = identity_matrix[:]
# for i in range(len(B)):
#     if B[-i-1] == '1':
#         temp = matrix[:]
#         while i != 0:
#             temp = matrix_mul(temp, temp)
#             i -= 1
#         result = matrix_mul(result, temp)

# for row in result:
#     print(*row)

from sys import stdin

n, b = map(int, stdin.readline().split())

def matrixMul(a, b):
    result = [[0]* n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += a[i][k]*b[k][j]
                result[i][j] %= 1000
    return result

matrix = [list(map(int, stdin.readline().split())) for _ in range(n)]

answer = [[1 if i == j else 0 for i in range(n)] for j in range(n)]

b = bin(b)[2:] #2진법으로 변환
for i in range(len(b)):
    if b[-i-1] == '1':
        temp = matrix[:]
        while i != 0:
            temp = matrixMul(temp, temp)
            i -= 1
        answer = matrixMul(answer, temp)

for row in answer:
    print(*row)
