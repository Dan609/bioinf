def Entropy(profile):
    n = len(profile['A'])
    profile_value=[]
    for i in range(n):
        m = 0
        for symbol in "ATCG":
            if profile[symbol][i]>m:
                m = profile[symbol][i]
        profile_value.append(m)
    import math
    results=0
    for i in range(n):
        results-=profile_value[i]*math.log(profile_value[i],2)
    return results
