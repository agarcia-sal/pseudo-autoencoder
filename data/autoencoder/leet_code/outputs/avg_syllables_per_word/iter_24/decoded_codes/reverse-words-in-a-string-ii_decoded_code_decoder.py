class Solution:
    def reverseWords(self, s):
        self.reverse_entire_list(s)
        start = 0
        for end in range(len(s)):
            if s[end] == ' ':
                self.reverse_sublist(s, start, end - 1)
                start = end + 1
        self.reverse_sublist(s, start, len(s) - 1)

    def reverse_entire_list(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    def reverse_sublist(self, lst, start_index, end_index):
        left, right = start_index, end_index
        while left < right:
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
            right -= 1