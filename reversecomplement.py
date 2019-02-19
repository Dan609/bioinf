def ReverseComplement(Pattern):
    # str.maketrans() is built in (Python 3.6, anyway); it maps any character in the first string to the one in the same position of the second
    trantab = str.maketrans("ATCG", "TAGC")
    # How to reverse a string in Python. You either know it or you don't, but once you know it you'll never forget it
    rev = Pattern[::-1]
    # Use the translation table defined above to do the complementary bit
    return rev.translate(trantab)
