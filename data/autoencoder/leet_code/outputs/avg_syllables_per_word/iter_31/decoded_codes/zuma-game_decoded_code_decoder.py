from collections import Counter
from math import inf

class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def clean(board: str) -> str:
            stack = []
            for ball in board:
                # Remove groups of 3 or more different from current ball
                while stack and stack[-1][0] != ball and stack[-1][1] >= 3:
                    stack.pop()
                if not stack or stack[-1][0] != ball:
                    stack.append([ball, 1])
                else:
                    stack[-1][1] += 1
            # Final cleanup if last group has 3 or more balls
            while stack and stack[-1][1] >= 3:
                stack.pop()
            # Reconstruct the cleaned board string
            result = []
            for char, count in stack:
                result.append(char * count)
            return ''.join(result)

        def dfs(board: str, hand_counter: Counter) -> int:
            if not board:
                return 0
            min_steps = inf
            i = 0
            length = len(board)
            while i < length:
                j = i + 1
                while j < length and board[j] == board[i]:
                    j += 1
                needed = 3 - (j - i)
                ball = board[i]
                if hand_counter[ball] >= needed:
                    new_hand = hand_counter.copy()
                    use = max(needed, 0)
                    # Only use if needed > 0, else they already have 3 or more in the board, no insertion needed
                    if use > 0:
                        new_hand[ball] -= use
                    # Form the new board by removing the interval [i, j)
                    new_board = clean(board[:i] + board[j:])
                    steps = dfs(new_board, new_hand)
                    if steps >= 0:
                        min_steps = min(min_steps, steps + use)
                i = j
            return -1 if min_steps == inf else min_steps

        hand_counter = Counter(hand)
        return dfs(board, hand_counter)