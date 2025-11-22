def count_and_say(n):
    if n == 1:
        return "1"
    seq = "1"
    for _ in range(2, n + 1):
        next_seq = ""
        count = 1
        prev = seq[0]
        for i in range(1, len(seq)):
            if seq[i] == prev:
                count += 1
            else:
                next_seq += str(count) + prev
                prev = seq[i]
                count = 1
        next_seq += str(count) + prev
        seq = next_seq
    return seq