from collections import defaultdict, deque
from typing import List, Dict, Set

class Solution:
    def alienOrder(self, list_of_words: List[str]) -> str:
        graph_mapping, indegree_mapping = self.InitializeGraphAndIndegree()
        set_of_all_characters = self.InitializeAllCharacters(list_of_words)

        n = len(list_of_words)
        for index in range(n - 1):
            word_one = list_of_words[index]
            word_two = list_of_words[index + 1]
            minimum_length = self.DetermineMinimumLength(len(word_one), len(word_two))
            found_difference = False

            for position in range(minimum_length):
                boolean_not_equal = self.CheckIfCharactersNotEqual(word_one[position], word_two[position])
                if boolean_not_equal:
                    boolean_is_absent = self.CheckIfNeighborAbsentInGraph(
                        graph_mapping, word_one[position], word_two[position])
                    if boolean_is_absent:
                        self.AddNeighborToGraph(graph_mapping, word_one[position], word_two[position])
                        self.IncrementIndegree(indegree_mapping, word_two[position], 1)
                    found_difference = True
                    break

            if not found_difference and len(word_one) > len(word_two):
                return ""

        # Initialize queue with all characters whose indegree is zero
        queue_structure = self.InitializeQueue(
            [ch for ch in set_of_all_characters if indegree_mapping[ch] == 0])

        result_order = []

        while queue_structure:
            current_character = self.PopLeftFromQueue(queue_structure)
            self.AppendItemToList(result_order, current_character)
            for neighbor_character in graph_mapping[current_character]:
                self.DecrementIndegree(indegree_mapping, neighbor_character, 1)
                if indegree_mapping[neighbor_character] == 0:
                    self.AppendItemToQueue(queue_structure, neighbor_character)

        if len(result_order) != len(set_of_all_characters):
            return ""

        return self.CallJoinCharacters(result_order)

    def InitializeGraphAndIndegree(self) -> (Dict[str, Set[str]], Dict[str, int]):
        graph_mapping = defaultdict(set)
        indegree_mapping = defaultdict(int)
        return graph_mapping, indegree_mapping

    def InitializeAllCharacters(self, list_of_words: List[str]) -> Set[str]:
        characters = set()
        for word in list_of_words:
            for ch in word:
                characters.add(ch)
        return characters

    def DetermineMinimumLength(self, len1: int, len2: int) -> int:
        return min(len1, len2)

    def CheckIfCharactersNotEqual(self, ch1: str, ch2: str) -> bool:
        return ch1 != ch2

    def CheckIfNeighborAbsentInGraph(
        self, graph_mapping: Dict[str, Set[str]], ch1: str, ch2: str
    ) -> bool:
        return ch2 not in graph_mapping[ch1]

    def AddNeighborToGraph(
        self, graph_mapping: Dict[str, Set[str]], ch1: str, ch2: str
    ) -> None:
        graph_mapping[ch1].add(ch2)

    def IncrementIndegree(self, indegree_mapping: Dict[str, int], ch: str, val: int) -> None:
        indegree_mapping[ch] += val

    def InitializeQueue(self, chars: List[str]) -> deque:
        return deque(chars)

    def PopLeftFromQueue(self, queue_structure: deque) -> str:
        return queue_structure.popleft()

    def AppendItemToList(self, result_order: List[str], ch: str) -> None:
        result_order.append(ch)

    def DecrementIndegree(self, indegree_mapping: Dict[str, int], ch: str, val: int) -> None:
        indegree_mapping[ch] -= val

    def AppendItemToQueue(self, queue_structure: deque, ch: str) -> None:
        queue_structure.append(ch)

    def CallJoinCharacters(self, result_order: List[str]) -> str:
        return "".join(result_order)