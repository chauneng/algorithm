from sys import stdin

m, d = list(map(int, stdin.readline().split()))
days = ['SUN','MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
m_Days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

print(days[(sum(m_Days[:m])+d) % 7])