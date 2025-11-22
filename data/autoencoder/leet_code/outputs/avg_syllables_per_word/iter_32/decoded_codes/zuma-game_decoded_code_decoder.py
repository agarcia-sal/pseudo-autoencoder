from collections import Counter
from math import inf

class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def clean(board: str) -> str:
            stack = []
            for ball in board:
                # If the last group in stack is of a different ball and count >=3, remove it
                while stack and stack[-1][0] != ball and stack[-1][1] >= 3:
                    stack.pop()
                if not stack or stack[-1][0] != ball:
                    stack.append([ball, 1])
                else:
                    stack[-1][1] += 1
            # After processing all balls, check the last group
            while stack and stack[-1][1] >= 3:
                stack.pop()
            # Rebuild string
            result = []
            for ball, count in stack:
                result.append(ball * count)
            return ''.join(result)

        def dfs(board: str, hand_counter: Counter) -> int:
            if not board:
                return 0
            min_steps = inf
            i = 0
            n = len(board)
            while i < n:
                j = i + 1
                # Find the segment of the same balls
                while j < n and board[j] == board[i]:
                    j += 1
                needed = 3 - (j - i)
                ball = board[i]
                if hand_counter[ball] >= needed:
                    new_hand = hand_counter.copy()
                    # Decrement used balls from hand, needed can be <=0 (means no balls needed)
                    # But as per logic, needed can be <=0 only if 3-(j-i) <=0, meaning the segment is already >=3,
                    # so no need insertion; but problem expects usage only when needed >0, so we can skip if needed<=0
                    if needed <= 0:
                        # no insertion needed, but this case not considered in original pseudocode, so skip it
                        # proceed to next segment
                        i = j
                        continue
                    new_hand[ball] -= needed
                    # remove balls inserted and the matched group and clean the board
                    new_board = clean(board[:i] + board[j:])
                    steps = dfs(new_board, new_hand)
                    if steps >= 0:
                        total_steps = steps + needed
                        if total_steps < min_steps:
                            min_steps = total_steps
                i = j
            return -1 if min_steps == inf else min_steps

        hand_counter = Counter(hand)
        return dfs(board, hand_counter)