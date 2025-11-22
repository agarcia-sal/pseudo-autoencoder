from collections import defaultdict

def find_repeated_sequences(s):
    seq_count = defaultdict(int)
    for i in range(len(s) - 9):
        seq = s[i:i+10]
        seq_count[seq] += 1
    res = [seq for seq, c in seq_count.items() if c > 1]
    return res