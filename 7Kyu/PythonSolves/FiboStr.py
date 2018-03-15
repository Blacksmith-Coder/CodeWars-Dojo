def solve(n):
    ret = []
    for i in range(n+1):
        if i == 0:
            ret.append(bin(i).replace('0b',''))
        if i == 1:
            ret.append(ret[i-1] + bin(i).replace('0b',''))
        if i > 1:
            ret.append(ret[i-1] + ret[i-2])
    return ret[n]


def solveRecurs(n):
    return "0" if n == 0 else "01" if n == 1 else solveRecurs(n-1) + solve(n-2)


