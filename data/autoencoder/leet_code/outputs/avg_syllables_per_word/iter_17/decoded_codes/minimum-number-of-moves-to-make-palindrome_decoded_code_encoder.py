class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        character_list = self.ConvertStringToList(s)
        total_moves = 0

        while len(character_list) > 1:
            found_pair = False
            for index in range(len(character_list) - 1, 0, -1):
                if character_list[index] == character_list[0]:
                    # Move the matched element to the end to pair off
                    for pos in range(index, len(character_list) - 1):
                        self.SwapElementsAtPositions(character_list, pos, pos + 1)
                        total_moves += 1
                    # Remove the paired elements at both ends
                    self.RemoveElementAtPosition(character_list, 0)
                    self.RemoveElementAtPosition(character_list, len(character_list) - 1)
                    found_pair = True
                    break
            if not found_pair:
                # No matching pair found for the first char, remove it (middle char case)
                self.RemoveElementAtPosition(character_list, 0)

        return total_moves

    def ConvertStringToList(self, string_input: str) -> list:
        # Convert string to list of characters
        return list(string_input)

    def SwapElementsAtPositions(self, collection: list, position_one: int, position_two: int) -> None:
        collection[position_one], collection[position_two] = collection[position_two], collection[position_one]

    def RemoveElementAtPosition(self, collection: list, position: int) -> None:
        del collection[position]