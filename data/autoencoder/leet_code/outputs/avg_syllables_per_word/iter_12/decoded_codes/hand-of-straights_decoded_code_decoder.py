from collections import Counter

class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        count = Counter(hand)
        unique_cards = sorted(count.keys())
        for card in unique_cards:
            needed = count[card]
            if needed > 0:
                for i in range(groupSize):
                    next_card = card + i
                    if count[next_card] < needed:
                        return False
                    count[next_card] -= needed
        return True