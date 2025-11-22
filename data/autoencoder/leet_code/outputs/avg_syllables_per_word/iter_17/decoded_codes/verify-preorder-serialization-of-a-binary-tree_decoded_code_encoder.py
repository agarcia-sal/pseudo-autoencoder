class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        nodes = preorder.split(',')
        slot_count = 1
        for node in nodes:
            if slot_count == 0:
                return False
            slot_count -= 1
            if node != '#':
                slot_count += 2
        return slot_count == 0