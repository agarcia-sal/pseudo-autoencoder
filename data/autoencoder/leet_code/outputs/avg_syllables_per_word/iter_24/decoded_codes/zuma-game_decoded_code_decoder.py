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
            if stack and stack[-1][1] >= 3:
                stack.pop()
            result = []
            for ball, count in stack:
                result.append(ball * count)
            return "".join(result)

        def dfs(board, hand_counter):
            if not board:
                return 0
            min_steps = float("inf")
            i = 0
            while i < len(board):
                j = i + 1
                while j < len(board) and board[j] == board[i]:
                    j += 1
                increment = 3 - (j - i)
                ball = board[i]
                if hand_counter[ball] >= increment:
                    new_hand_counter = hand_counter.copy()
                    new_hand_counter[ball] -= increment
                    if new_hand_counter[ball] == 0:
                        del new_hand_counter[ball]
                    new_board = clean(board[:i] + board[j:])
                    steps = dfs(new_board, new_hand_counter)
                    if steps >= 0:
                        min_steps = min(min_steps, steps + increment)
                i = j
            return -1 if min_steps == float("inf") else min_steps

        hand_counter = Counter(hand)
        return dfs(board, hand_counter)