from collections import Counter

def is_possible(nums):
    freq = Counter(nums)
    end_seq = Counter()

    for x in nums:
        if freq[x] == 0:
            continue

        if end_seq[x-1] > 0:
            end_seq[x-1] -= 1
            end_seq[x] += 1
        elif freq[x+1] > 0 and freq[x+2] > 0:
            freq[x+1] -= 1
            freq[x+2] -= 1
            end_seq[x+2] += 1
        else:
            return False

        freq[x] -= 1

    return True