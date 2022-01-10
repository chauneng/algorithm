a, b = "1010", "1011"
max_digit = (max(len(list(a)), len(list(b)))+1)
tmp_res = [0]*max_digit

tmp_a = [0]*(max_digit-len(list(a)))
tmp_a.extend(list(a))
tmp_b = [0]*(max_digit-len(list(b)))
tmp_b.extend(list(b))
tmp = 0

for i in range(max_digit-1, -1, -1):
    tmp_sum = int(tmp_a[i]) + int(tmp_b[i]) + tmp
    if tmp_sum == 2:
        tmp = 1
        tmp_res[i] = "0"
    elif tmp_sum == 3:
        tmp = 1
        tmp_res[i] = "1"
    else:
        tmp_res[i] = str(tmp_sum)

res = str(int("".join(tmp_res)))

print(res)