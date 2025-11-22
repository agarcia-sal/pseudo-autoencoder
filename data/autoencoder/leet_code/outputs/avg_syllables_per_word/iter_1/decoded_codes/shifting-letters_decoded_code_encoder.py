for i in range(len(shifts) - 2, -1, -1):
    shifts[i] += shifts[i + 1]
result = []
for i in range(len(s)):
    c = chr((ord(s[i]) - ord('a') + shifts[i]) % 26 + ord('a'))
    result.append(c)
return "".join(result)