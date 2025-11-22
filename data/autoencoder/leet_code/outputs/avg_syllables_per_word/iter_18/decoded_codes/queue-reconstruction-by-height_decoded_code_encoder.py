from typing import List

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # Sort by height descending (-x[0]) and then by k ascending (x[1])
        people.sort(key=lambda x: (-x[0], x[1]))
        queue = []
        for person in people:
            queue.insert(person[1], person)
        return queue