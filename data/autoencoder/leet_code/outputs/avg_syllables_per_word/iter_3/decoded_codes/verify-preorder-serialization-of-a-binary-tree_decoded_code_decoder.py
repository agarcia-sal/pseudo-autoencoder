class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        slots = 1
        for node in preorder.split(','):
            if slots == 0:
                return False
            slots -= 1
            if node != '#':
                slots += 2
        return slots == 0