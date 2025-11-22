class Solution:
    def findPermutation(self, s: str) -> list[int]:
        result = [i + 1 for i in range(len(s) + 1)]
        start = 0
        for end_index in range(len(s) + 1):
            if end_index == len(s) or s[end_index] == 'I':
                self.reverseSegment(result, start, end_index)
                start = end_index + 1
        return result

    def reverseSegment(self, collection: list[int], start_position: int, end_position: int) -> None:
        left_pointer, right_pointer = start_position, end_position
        while left_pointer < right_pointer:
            collection[left_pointer], collection[right_pointer] = collection[right_pointer], collection[left_pointer]
            left_pointer += 1
            right_pointer -= 1