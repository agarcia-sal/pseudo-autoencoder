from typing import List

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        nodes: List[str] = preorder.split(',')
        slots: int = 1
        for node in nodes:
            if slots == 0:
                return False
            slots -= 1
            if node != '#':
                slots += 2
        return slots == 0