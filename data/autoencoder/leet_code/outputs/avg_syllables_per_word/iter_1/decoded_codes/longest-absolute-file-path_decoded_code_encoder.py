def length_longest_path(input):
    lines = input.split('\n')
    stack = []
    max_len = 0

    for line in lines:
        depth = line.count('\t')
        name = line[depth:]
        while len(stack) > depth:
            stack.pop()
        cur_len = (stack[-1] + len(name) + 1) if stack else len(name)
        if '.' in name:
            max_len = max(max_len, cur_len)
        else:
            stack.append(cur_len)

    return max_len