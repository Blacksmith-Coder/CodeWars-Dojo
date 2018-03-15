
def DNA_strand(dna):
    i = 0
    ret = ""
    while i < len(dna):
        if dna[i] == 'A':
            ret += 'T'
        elif dna[i] == 'T':
            ret += 'A'
        elif dna[i] == 'G':
            ret += 'C'
        else :
            ret += 'G'
        i = i + 1
    return ret


chaine = "AAATTGGGCCC"
print(DNA_strand(chaine))


