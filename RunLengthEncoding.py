s = '111122233333311112222'
frequency = 1
l = ''
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        l = s[i - 1]
        frequency +=1
    else:
        print("(", l, ",", frequency, ")")
        frequency = 1
print("(", l, ",", frequency, ")")

