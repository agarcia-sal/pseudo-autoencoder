from collections import Counter

class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        unique_cards = sorted(count)

        for card in unique_cards:
            needed = count[card]
            if needed > 0:
                for i in range(groupSize):
                    if count[card + i] < needed:
                        return False
                    count[card + i] -= needed
        return True