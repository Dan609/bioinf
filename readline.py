import os
os.getcwd()

f = open('dataset_5_6.txt','r')
g = open('output.txt','w')
i=0
for line in f:
    if i % 2 == 0:
        g.write(str(line))
    i = i + 1
f.close()
g.close()
