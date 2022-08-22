# put your python code here

n, m = [int(x) for x in input().split()]
a = [x + 1 for x in range(n * m)]
s = [[0] * m for _ in range(n)]




for d in range((min(n, m) // 2) + 1):
    for i in range(m - 1 - 2 * d):  # -->
        if len(a) == 0:
            break
        s[d][i + d] = a.pop(0)
    for i in range(n - 1 - 2 * d):  # \/
        if len(a) == 0: break
        s[i + d][m - 1 - d] = a.pop(0)
    for i in range(m - 1 - d, d, -1):  # <--
        if len(a) == 0: break
        s[n - 1 - d][i] = a.pop(0)
    for i in range(n - 1 - d, d, -1):  # /\
        if len(a) == 0: break
        s[i][d] = a.pop(0)
if n == m and n % 2 != 0:    s[n // 2][n // 2] = a.pop(0)
for x in s:    print(*[str(i).rjust(2) for i in x])
