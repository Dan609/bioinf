def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        freq[Pattern] = 0
        for i in range(n-k+1):
            if Text[i:i+k] == Pattern:
                freq[Pattern] = freq[Pattern] + 1
    return freq

# variant

def FrequencyMap(Text, k):
        freq = {}
        n = len(Text)
        for i in range(n-k+1):
            Pattern = Text[i:i+k]
            freq[Pattern] = freq.get(Pattern,0)+1
        return freq
