# The following lines will automatically read in the Vibrio cholerae genome for you and store it in a variable named v_cholerae
import sys                              # needed to read the genome
input = sys.stdin.read().splitlines()   #
v_cholerae = input[1]                   # store the genome as 'v_cholerae'


# Call PatternMatching with Pattern equal to "CTTGATCAT" and Genome equal to v_cholerae,
# and store the output as a variable called positions


def PatternMatching("CTTGATCAT", v_cholerae):
    positions = [] # output variable
    for i in range(len(Genome)-len(Pattern)+1):
        if Genome[i:i+len(Pattern)] == Pattern :
            positions.append(i)

    return positions

# print the positions variable
print (PatternMatching("CTTGATCAT", v_cholerae))

####

# The following lines will automatically read in the Vibrio cholerae genome for you and store it in a variable named v_cholerae
import sys                              # needed to read the genome
input = sys.stdin.read().splitlines()   #
v_cholerae = input[1]                   # store the genome as 'v_cholerae'


# Call PatternMatching with Pattern equal to "CTTGATCAT" and Genome equal to v_cholerae,
# and store the output as a variable called positions


def PatternMatching("CTTGATCAT", v_cholerae):
    positions = [] # output variable
    for i in range(len(Genome)-len("CTTGATCAT")+1):
        if v_cholerae[i:i+len("CTTGATCAT")] == "CTTGATCAT" :
            positions.append(i)

    return positions

# print the positions variable
print (PatternMatching("CTTGATCAT", v_cholerae))
