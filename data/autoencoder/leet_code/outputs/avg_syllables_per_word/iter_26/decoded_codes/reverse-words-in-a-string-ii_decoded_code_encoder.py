class Solution:
    def reverseWords(self, list_of_characters):
        # Helper function to reverse a subsection of the list in place
        def reverse_sublist(lst, left, right):
            while left < right:
                lst[left], lst[right] = lst[right], lst[left]
                left += 1
                right -= 1

        reverse_sublist(list_of_characters, 0, len(list_of_characters) - 1)

        start = 0
        for end in range(len(list_of_characters)):
            if list_of_characters[end] == ' ':
                reverse_sublist(list_of_characters, start, end - 1)
                start = end + 1

        reverse_sublist(list_of_characters, start, len(list_of_characters) - 1)