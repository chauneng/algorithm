import sys
#100보다 작은 수는 전부 각 자리수가 등차수열이다.
num = sys.stdin.readline()
if int(num) < 100 :
    print(num)
else :
    cnt = 99
    for i in range(100 ,int(num)) :
        diff = int(num[1])-int(num[0])
        i = str(i)

        for j in range(len(str(i))-1, 1, -1) :

            if int(num[j])-int(num[j-1]) == diff :
                cnt =+ 1
    print(cnt)
