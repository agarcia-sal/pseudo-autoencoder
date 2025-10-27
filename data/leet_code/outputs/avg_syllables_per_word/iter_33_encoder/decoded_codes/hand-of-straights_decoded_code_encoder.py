from collections import Counter

class Solution:
    def isNStraightHand(self, hand, groupSize):
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        unique_cards = sorted(count)

        for card in unique_cards:
            if count[card] > 0:
                needed = count[card]
                for i in range(groupSize):
                    next_card = card + i
                    if count[next_card] < needed:
                        return False
                    count[next_card] -= needed

        return True