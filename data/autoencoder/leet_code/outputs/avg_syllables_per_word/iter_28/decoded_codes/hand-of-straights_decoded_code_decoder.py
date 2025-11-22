from collections import Counter
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        count = Counter(hand)
        unique_cards = sorted(count.keys())
        for card in unique_cards:
            needed = count[card]
            if needed > 0:
                for i in range(groupSize):
                    if count.get(card + i, 0) < needed:
                        return False
                    count[card + i] -= needed
        return True