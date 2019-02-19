def ReverseComplement(Pattern):
    Pattern = Reverse(Pattern) # reverse all letters in a string
    Pattern = Complement(Pattern) # complement each letter in a string
    return Pattern



rev = ''.join(reversed(Pattern))


def Reverse(Pattern):
    rev = ""
    for i in range(len(Pattern)-1, -1, -1):
        rev = rev + Pattern[i]
    return rev


def Complement(Pattern):
    basepairs = {"A":"T", "G":"C", "T":"A", "C":"G"}
    complement = ""
    for base in Pattern:
        complement += basepairs.get(base)
    return complement
