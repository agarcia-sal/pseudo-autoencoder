from typing import List

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        self.sort_people_by_height_descending_and_k_ascending(people)
        queue = []
        for person in people:
            self.insert_person_into_queue_at_k_position(queue, person)
        return queue

    def sort_people_by_height_descending_and_k_ascending(self, people: List[List[int]]) -> None:
        people.sort(key=lambda x: (-x[0], x[1]))

    def insert_person_into_queue_at_k_position(self, queue: List[List[int]], person: List[int]) -> None:
        queue.insert(person[1], person)