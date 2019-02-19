s = open('dataset_31_6.txt', 'r').read().replace('\n', ' ')

word_freq = {}

for word in s.split(' '): word_freq[word] = 0

for word in s.split(' '): word_freq[word] += 1

for k, v in word_freq.items():

    print(k," ",v)
