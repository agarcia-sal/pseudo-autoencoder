def get_max_repetitions(s1, n1, s2, n2):
    s2_count = [0] * (n1 + 1)
    index_map = [0] * (n1 + 1)
    cur = 0
    s1_count = 0
    while s1_count < n1:
        s1_count += 1
        for c in s1:
            if c == s2[cur]:
                cur += 1
                if cur == len(s2):
                    s2_count[s1_count] = s2_count[s1_count - 1] + 1
                    cur = 0
        index_map[s1_count] = cur
        if cur in index_map[:s1_count]:
            start = index_map.index(cur)
            cycle_len = s1_count - start
            cycles = (n1 - start) // cycle_len
            rem = (n1 - start) % cycle_len
            total = (s2_count[start] +
                     cycles * (s2_count[start + cycle_len] - s2_count[start]) +
                     s2_count[start + rem] - s2_count[start])
            return total // n2
        s2_count[s1_count] = s2_count[s1_count - 1]
    return s2_count[s1_count] // n2