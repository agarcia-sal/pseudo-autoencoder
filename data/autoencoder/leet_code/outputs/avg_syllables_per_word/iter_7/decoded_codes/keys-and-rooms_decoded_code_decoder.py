from typing import List, Set

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited: Set[int] = set()
        stack: List[int] = [0]

        while stack:
            current_room = stack.pop()
            visited.add(current_room)
            for key in rooms[current_room]:
                if key not in visited:
                    stack.append(key)

        return len(visited) == len(rooms)