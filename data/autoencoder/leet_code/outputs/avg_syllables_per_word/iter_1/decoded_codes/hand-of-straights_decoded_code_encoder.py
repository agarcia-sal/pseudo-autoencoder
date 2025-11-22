from collections import Counter

def isNStraightHand(hand, groupSize):
    if len(hand) % groupSize != 0:
        return False
    count = Counter(hand)

    for card in sorted(count.keys()):
        if count[card] > 0:
            needed = count[card]
            for i in range(groupSize):
                if count[card + i] < needed:
                    return False
                count[card + i] -= needed
    return True