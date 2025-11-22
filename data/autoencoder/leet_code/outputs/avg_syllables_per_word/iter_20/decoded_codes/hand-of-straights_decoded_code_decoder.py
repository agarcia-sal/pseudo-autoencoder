from collections import Counter
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        unique_cards = sorted(count.keys())

        for card in unique_cards:
            if count[card] > 0:
                needed = count[card]
                for offset in range(groupSize):
                    next_card = card + offset
                    if count[next_card] < needed:
                        return False
                    count[next_card] -= needed
        return True