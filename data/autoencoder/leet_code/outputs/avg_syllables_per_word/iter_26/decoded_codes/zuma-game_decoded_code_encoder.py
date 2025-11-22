from collections import Counter
from math import inf

class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def clean(current_board: str) -> str:
            stack = []
            for ball in current_board:
                # If last group has >=3 balls and ball is different, remove the group
                while stack and stack[-1][0] != ball and stack[-1][1] >= 3:
                    stack.pop()
                if not stack or stack[-1][0] != ball:
                    stack.append([ball, 1])
                else:
                    stack[-1][1] += 1
            # After loop, remove last group if >=3
            if stack and stack[-1][1] >= 3:
                stack.pop()
            # Reconstruct the board string
            return ''.join(ball * count for ball, count in stack)

        def dfs(current_board: str, current_hand_counter: Counter) -> int:
            if not current_board:
                return 0  # board cleared
            min_steps = inf
            i = 0
            length = len(current_board)
            while i < length:
                j = i + 1
                while j < length and current_board[j] == current_board[i]:
                    j += 1
                needed = 3 - (j - i)
                ball = current_board[i]
                if current_hand_counter[ball] >= needed and needed > 0:
                    new_hand_counter = current_hand_counter.copy()
                    new_hand_counter[ball] -= needed
                    new_board = clean(current_board[:i] + current_board[j:])
                    steps = dfs(new_board, new_hand_counter)
                    if steps >= 0:
                        min_steps = min(min_steps, steps + needed)
                elif needed <= 0:
                    # Already 3 or more balls, no need to insert from hand, just clean and dfs
                    new_board = clean(current_board[:i] + current_board[j:])
                    steps = dfs(new_board, current_hand_counter)
                    if steps >= 0:
                        min_steps = min(min_steps, steps)
                i = j
            return -1 if min_steps == inf else min_steps

        hand_counter = Counter(hand)
        return dfs(board, hand_counter)