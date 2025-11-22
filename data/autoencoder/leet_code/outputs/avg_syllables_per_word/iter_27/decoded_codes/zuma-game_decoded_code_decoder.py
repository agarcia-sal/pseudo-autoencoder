from collections import Counter
from math import inf
from typing import Counter as CounterType


class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def clean(board: str) -> str:
            stack = []
            for ball in board:
                if stack and stack[-1][0] != ball and stack[-1][1] >= 3:
                    stack.pop()
                if not stack or stack[-1][0] != ball:
                    stack.append([ball, 1])
                else:
                    stack[-1][1] += 1
            if stack and stack[-1][1] >= 3:
                stack.pop()
            result = ''.join(ball * count for ball, count in stack)
            # Recursively clean after removals to handle chain reactions
            if len(result) < len(board):
                return clean(result)
            return result

        def dfs(board: str, hand_counter: CounterType[str]) -> int:
            if not board:
                return 0
            min_steps = inf
            i = 0
            n = len(board)
            while i < n:
                j = i + 1
                while j < n and board[j] == board[i]:
                    j += 1
                need = 3 - (j - i)
                ball = board[i]
                if hand_counter[ball] >= need:
                    new_hand_counter = hand_counter.copy()
                    new_hand_counter[ball] -= need
                    new_board = clean(board[:i] + board[j:])
                    steps = dfs(new_board, new_hand_counter)
                    if steps >= 0:
                        total_steps = steps + need
                        if total_steps < min_steps:
                            min_steps = total_steps
                i = j
            return -1 if min_steps == inf else min_steps

        hand_counter = Counter(hand)
        return dfs(board, hand_counter)