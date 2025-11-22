class Solution:
    def reverseWords(self, list_of_characters) -> None:
        list_of_characters.reverse()
        start_position = 0
        for index_position in range(len(list_of_characters)):
            if list_of_characters[index_position] == ' ':
                list_of_characters[start_position:index_position] = reversed(list_of_characters[start_position:index_position])
                start_position = index_position + 1
        list_of_characters[start_position:] = reversed(list_of_characters[start_position:])