class Solution:
    def reconstructQueue(self, people):
        # Sort people by descending height and ascending k
        people.sort(key=lambda x: (-x[0], x[1]))
        queue = []
        for person in people:
            queue.insert(person[1], person)
        return queue