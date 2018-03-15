def solve(st, a, b):
    b = len(st) if b > len(st) - 1 else b
    return st[:a] + st[a:b+1][::-1] + st[b+1:]


chn = "codewars"
print(chn)
print(solve(chn, 1, 5))


