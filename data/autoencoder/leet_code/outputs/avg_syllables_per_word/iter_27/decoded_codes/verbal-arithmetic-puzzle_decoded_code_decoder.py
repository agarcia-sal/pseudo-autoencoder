from typing import List, Set, Dict

class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        collection_of_unique_characters: Set[str] = set()
        for word in words:
            collection_of_unique_characters.update(word)
        collection_of_unique_characters.update(result)

        if len(collection_of_unique_characters) > 10:
            return False

        collection_of_characters_that_cannot_be_zero: Set[str] = set()
        for word in words:
            if len(word) > 1:
                collection_of_characters_that_cannot_be_zero.add(word[0])
        if len(result) > 1:
            collection_of_characters_that_cannot_be_zero.add(result[0])

        mapping_from_character_to_digit: Dict[str, int] = {}
        mapping_from_digit_to_character: Dict[int, str] = {}

        def can_assign(character: str, digit: int) -> bool:
            return (character not in mapping_from_character_to_digit and
                    (digit not in mapping_from_digit_to_character or mapping_from_digit_to_character[digit] == character))

        def assign(character: str, digit: int) -> None:
            mapping_from_character_to_digit[character] = digit
            mapping_from_digit_to_character[digit] = character

        def unassign(character: str, digit: int) -> None:
            mapping_from_character_to_digit.pop(character, None)
            mapping_from_digit_to_character.pop(digit, None)

        def word_value(word: str) -> int:
            total_value = 0
            length = len(word)
            for index, character in enumerate(reversed(word)):
                total_value += mapping_from_character_to_digit.get(character, 0) * (10 ** index)
            return total_value

        max_word_len = max((len(word) for word in words), default=0)
        max_len = max(max_word_len, len(result))

        def backtrack(index: int, column: int, sum_of_column: int) -> bool:
            if column >= max_len:
                return sum_of_column == 0

            if index == len(words):
                if column < len(result):
                    character_at_position = result[len(result) - 1 - column]
                    digit_needed = sum_of_column % 10
                    if character_at_position in mapping_from_character_to_digit:
                        if mapping_from_character_to_digit[character_at_position] == digit_needed:
                            return backtrack(0, column + 1, sum_of_column // 10)
                        else:
                            return False
                    else:
                        if (can_assign(character_at_position, digit_needed) and
                                (digit_needed != 0 or character_at_position not in collection_of_characters_that_cannot_be_zero)):
                            assign(character_at_position, digit_needed)
                            if backtrack(0, column + 1, sum_of_column // 10):
                                return True
                            unassign(character_at_position, digit_needed)
                        return False
                else:
                    return sum_of_column == 0

            current_word = words[index]
            if column >= len(current_word):
                return backtrack(index + 1, column, sum_of_column)

            current_character = current_word[len(current_word) - 1 - column]
            if current_character in mapping_from_character_to_digit:
                return backtrack(index + 1, column, sum_of_column + mapping_from_character_to_digit[current_character])

            for digit in range(10):
                if can_assign(current_character, digit) and (digit != 0 or current_character not in collection_of_characters_that_cannot_be_zero):
                    assign(current_character, digit)
                    if backtrack(index + 1, column, sum_of_column + digit):
                        return True
                    unassign(current_character, digit)

            return False

        return backtrack(0, 0, 0)