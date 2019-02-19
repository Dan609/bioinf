def SkewArray(Genome):
    skew = {}
    skew[0] = 0
    for i in range (len(Genome)):
        if Genome[i] == "A" or Genome[i] == "T":
            skew[i + 1] = skew [i]
        elif Genome[i] == "G":
            skew[i + 1] = skew[i] + 1
        else:
            skew[i + 1] = skew[i] - 1
    return skew



def MinimumSkew(Genome):
    positions = []
    sk = SkewArray(Genome)
    m = min(sk.values())
    for key in sk:
        if sk[key] == m:
            positions.append(key)

    return positions

print(MinimumSkew("GATACACTTCCCGAGTAGGTACTG" ))
