from typing import List

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # Sort the list so that people with higher height come first,
        # and if heights are equal, sort by increasing k-value.
        people.sort(key=lambda x: (-x[0], x[1]))
        queue = []
        for person in people:
            queue.insert(person[1], person)
        return queue