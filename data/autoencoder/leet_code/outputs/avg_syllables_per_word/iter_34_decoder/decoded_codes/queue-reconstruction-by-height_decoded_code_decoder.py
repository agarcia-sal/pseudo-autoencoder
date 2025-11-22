from typing import List

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # Sort by height descending and k ascending
        people.sort(key=lambda person: (-person[0], person[1]))
        queue = []
        for person in people:
            queue.insert(person[1], person)
        return queue