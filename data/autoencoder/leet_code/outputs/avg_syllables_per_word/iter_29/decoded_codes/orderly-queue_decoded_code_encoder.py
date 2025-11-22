class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1:
            return ''.join(sorted(s))
        length_of_string = len(s)
        smallest_rotation = s
        for index in range(1, length_of_string):
            rotated_string = s[index:] + s[:index]
            if rotated_string < smallest_rotation:
                smallest_rotation = rotated_string
        return smallest_rotation