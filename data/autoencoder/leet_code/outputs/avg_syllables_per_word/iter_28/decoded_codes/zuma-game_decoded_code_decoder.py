from collections import Counter
from math import inf
from copy import deepcopy

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
            return "".join(ball * count for ball, count in stack)

        def dfs(board: str, hand_counter: Counter) -> int:
            if not board:
                return 0
            min_steps = inf
            i = 0
            while i < len(board):
                j = i + 1
                while j < len(board) and board[j] == board[i]:
                    j += 1
                needed = 3 - (j - i)
                if hand_counter[board[i]] >= needed:
                    new_hand = hand_counter.copy()
                    new_hand[board[i]] -= needed
                    if new_hand[board[i]] == 0:
                        del new_hand[board[i]]
                    new_board = clean(board[:i] + board[j:])
                    steps = dfs(new_board, new_hand)
                    if steps >= 0:
                        min_steps = min(min_steps, steps + needed)
                i = j
            return -1 if min_steps == inf else min_steps

        hand_counter = Counter(hand)
        return dfs(board, hand_counter)