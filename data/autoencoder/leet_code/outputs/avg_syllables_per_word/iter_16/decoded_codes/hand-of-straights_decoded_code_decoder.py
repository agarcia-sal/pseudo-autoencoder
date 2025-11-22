from collections import Counter

class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        unique_cards = sorted(count.keys())

        for card in unique_cards:
            if count[card] > 0:
                needed = count[card]
                for i in range(groupSize):
                    current = card + i
                    if count[current] < needed:
                        return False
                    count[current] -= needed

        return True