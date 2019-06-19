s = '89400000000000000000000000000000000'
frequency = 1
noFrequency = ''
for i in range(1, len(s)):
    if s[i-1] != s[i]:
        noFrequency += s[i-1]
    else:
        frequency += 1
srs = str(noFrequency)+'f'+str(frequency)
print(srs)




