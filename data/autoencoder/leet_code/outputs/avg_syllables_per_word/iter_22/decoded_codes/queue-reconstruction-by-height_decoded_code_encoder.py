from typing import List

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # Sort by height descending, and for same height by k ascending
        people.sort(key=lambda x: (-x[0], x[1]))
        queue = []
        for person in people:
            # Insert person at index equal to their k value
            queue.insert(person[1], person)
        return queue