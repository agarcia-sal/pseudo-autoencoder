count_letter = s.count(letter)
stack = []
repetition = count_letter
for i, c in enumerate(s):
    while stack and c < stack[-1] and len(s) - i + len(stack) - 1 >= k:
        if stack[-1] == letter:
            if count_letter > repetition:
                repetition += 1
                stack.pop()
            else:
                break
        else:
            stack.pop()
    if len(stack) < k:
        if c == letter:
            stack.append(c)
            repetition -= 1
        elif k - len(stack) > repetition:
            stack.append(c)
    if c == letter:
        count_letter -= 1
while len(stack) < k:
    stack.append(letter)
return ''.join(stack)