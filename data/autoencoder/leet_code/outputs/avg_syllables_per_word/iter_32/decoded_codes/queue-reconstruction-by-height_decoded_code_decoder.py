from typing import List

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        self.sort_people_by_height_descending_and_k_ascending(people)
        queue = []
        for person in people:
            self.insert_person_at_position_specified_by_k(queue, person)
        return queue

    def sort_people_by_height_descending_and_k_ascending(self, people: List[List[int]]) -> None:
        # Sort by height descending, then k ascending
        people.sort(key=lambda x: (-x[0], x[1]))

    def insert_person_at_position_specified_by_k(self, queue: List[List[int]], person: List[int]) -> None:
        # Insert person at index = k
        queue.insert(person[1], person)