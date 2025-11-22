from collections import Counter

class Solution:
    def isPossible(self, list_of_numbers) -> bool:
        num_count = Counter(list_of_numbers)
        end_with = Counter()

        for num in list_of_numbers:
            if num_count[num] == 0:
                continue
            if end_with[num - 1] > 0:
                end_with[num - 1] -= 1
                end_with[num] += 1
            elif num_count[num + 1] > 0 and num_count[num + 2] > 0:
                num_count[num + 1] -= 1
                num_count[num + 2] -= 1
                end_with[num + 2] += 1
            else:
                return False
            num_count[num] -= 1

        return True