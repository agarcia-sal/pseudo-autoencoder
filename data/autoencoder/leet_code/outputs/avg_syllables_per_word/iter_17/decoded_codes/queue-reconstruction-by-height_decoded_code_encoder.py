class Solution:
    def reconstructQueue(self, list_of_people):
        # Sort people by descending height and ascending k-value
        list_of_people.sort(key=lambda person: (-person[0], person[1]))
        queue = []
        for person in list_of_people:
            queue.insert(person[1], person)
        return queue