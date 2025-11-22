class Solution:
    def singleNumber(self, list_of_numbers):
        ones = 0
        twos = 0
        for number in list_of_numbers:
            # Update ones with bits that have appeared once so far
            ones = (ones ^ number) & ~twos
            # Update twos with bits that have appeared twice so far
            twos = (twos ^ number) & ~ones
        return ones