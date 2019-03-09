a = input()
print("A", a.count('A'))
print("G", a.count('G'))
print("C", a.count('C'))
print("T", a.count('T'))


a = input()
print("A", round(a.count('A')/len(a), 2))
print("G", round(a.count('G')/len(a), 2))
print("C", round(a.count('C')/len(a), 2))
print("T", round(a.count('T')/len(a), 2))

print((lambda a: (a.count('C') + a.count('G')) / len(a) * 100)(str(input()).upper()))


string = input()
guanin = string.lower().count('g')
cytosin = string.lower().count('c')
print(((guanin + cytosin) / len(string)) * 100 )



# Output: A consensus string of Motifs.
def Consensus(Motifs):
    consensus = ""
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
