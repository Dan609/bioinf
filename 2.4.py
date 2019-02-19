def SkewArray(Genome):
    ccount = 0
    output = [0]
    for g in Genome:
        if (g == 'C'):
            ccount -= 1
        elif (g == 'G'):
            ccount += 1
        output.append(ccount)
    return output


####

def SkewArray(Genome):
    skew = [0]
    score = {"A":0, "T":0, "C":-1, "G":1}
    for i in range(1,len(Genome)+1):
            skew.append(score[Genome[i-1]] + skew[i-1])
    return skew


###
def MinimumSkew(Genome):
    positions = []
    sk = SkewArray(Genome)
    m = min(sk.values())
    for key in sk:
        if sk[key] == m:
            positions.append(key)

    return positions



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
