class Solution:
    def isScramble(self, string_one: str, string_two: str) -> bool:
        if string_one == string_two:
            return True

        if sorted(string_one) != sorted(string_two):
            return False

        length_n = len(string_one)

        for index_i in range(1, length_n):
            # Check without swap
            if (self.isScramble(string_one[:index_i], string_two[:index_i]) and
                self.isScramble(string_one[index_i:], string_two[index_i:])):
                return True

            # Check with swap
            if (self.isScramble(string_one[:index_i], string_two[-index_i:]) and
                self.isScramble(string_one[index_i:], string_two[:-index_i])):
                return True

        return False