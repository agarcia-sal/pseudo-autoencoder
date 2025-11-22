from collections import Counter

class Solution:
    def findMinStep(self, board, hand):
        def clean(board):
            stack = []
            for ball in board:
                while stack and stack[-1][0] != ball and stack[-1][1] >= 3:
                    stack.pop()
                if not stack or stack[-1][0] != ball:
                    stack.append([ball, 1])
                else:
                    stack[-1][1] += 1
            while stack and stack[-1][1] >= 3:
                stack.pop()
            return ''.join(ball * count for ball, count in stack)

        def dfs(board, hand_counter):
            if not board:
                return 0
            min_steps = float('inf')
            i = 0
            n = len(board)
            while i < n:
                j = i + 1
                while j < n and board[j] == board[i]:
                    j += 1
                need = 3 - (j - i)
                ball = board[i]
                if hand_counter[ball] >= need:
                    new_hand = hand_counter.copy()
                    new_hand[ball] -= need
                    new_board = clean(board[:i] + board[j:])
                    steps = dfs(new_board, new_hand)
                    if steps >= 0:
                        min_steps = min(min_steps, steps + need)
                i = j
            return -1 if min_steps == float('inf') else min_steps

        hand_counter = Counter(hand)
        return dfs(board, hand_counter)