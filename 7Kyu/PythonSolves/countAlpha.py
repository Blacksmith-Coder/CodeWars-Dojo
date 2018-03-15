def solve(arr):
    ref = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ret = []
    for chn in arr:
        chn = chn.upper()
        count = 0
        for i in range(len(ref)):
            for j in range(len(chn)):
                if i == j and ref[i] == chn[j]:
                    count = count + 1
        ret.append(count)
    return ret


test = ["IAMDEFANDJKL","thedefgh","xyzDEFghijabc"]
print(solve(test))