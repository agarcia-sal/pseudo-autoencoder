class Solution:
    def magicalString(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 3:
            return 1

        s = [1, 2, 2]
        count = 1  # count of '1's in s
        index = 2

        while len(s) < n:
            next_num = 3 - s[-1]  # toggles between 1 and 2
            self.ExtendList(s, next_num, s[index])
            if next_num == 1:
                count += s[index]
            index += 1

        if len(s) > n:
            excess_length = len(s) - n
            last_element = s[-1]
            count -= last_element * excess_length

        return count

    def ExtendList(self, list_to_extend, number, times):
        list_to_extend.extend([number] * times)