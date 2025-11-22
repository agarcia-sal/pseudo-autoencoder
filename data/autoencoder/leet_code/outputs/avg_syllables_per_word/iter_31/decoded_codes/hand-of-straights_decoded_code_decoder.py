from collections import Counter

class Solution:
    def isNStraightHand(self, hand, groupSize) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        unique_cards = sorted(count.keys())

        for card in unique_cards:
            needed = count[card]
            if needed > 0:
                for i in range(groupSize):
                    current_card = card + i
                    if count.get(current_card, 0) < needed:
                        return False
                    count[current_card] -= needed

        return True