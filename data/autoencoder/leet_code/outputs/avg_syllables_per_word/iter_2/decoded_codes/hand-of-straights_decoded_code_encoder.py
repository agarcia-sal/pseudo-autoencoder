from collections import Counter

class Solution:
    def isNStraightHand(self, hand, groupSize):
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        unique_cards = sorted(count.keys())

        for card in unique_cards:
            if count[card] > 0:
                needed = count[card]
                for i in range(groupSize):
                    if count[card + i] < needed:
                        return False
                    count[card + i] -= needed

        return True