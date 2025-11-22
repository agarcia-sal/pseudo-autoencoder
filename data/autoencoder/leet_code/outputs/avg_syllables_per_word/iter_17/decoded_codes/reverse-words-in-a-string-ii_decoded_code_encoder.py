class Solution:
    def reverseWords(self, list_of_characters):
        list_of_characters.reverse()
        start = 0
        for end in range(len(list_of_characters)):
            if list_of_characters[end] == ' ':
                self.reverseWordsInPlace(list_of_characters, start, end - 1)
                start = end + 1
        self.reverseWordsInPlace(list_of_characters, start, len(list_of_characters) - 1)

    def reverseWordsInPlace(self, list_of_characters, start_index, end_index):
        left, right = start_index, end_index
        while left < right:
            list_of_characters[left], list_of_characters[right] = list_of_characters[right], list_of_characters[left]
            left += 1
            right -= 1