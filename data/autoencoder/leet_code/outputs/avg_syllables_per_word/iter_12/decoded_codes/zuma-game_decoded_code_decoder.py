from collections import Counter

class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def clean(board: str) -> str:
            stack = []
            for ball in board:
                # If top of stack is different ball and count >= 3, remove it (pop)
                while stack and stack[-1][0] != ball and stack[-1][1] >= 3:
                    stack.pop()
                if not stack or stack[-1][0] != ball:
                    stack.append([ball, 1])
                else:
                    stack[-1][1] += 1
            # Check again after processing all balls
            while stack and stack[-1][1] >= 3:
                stack.pop()
            result = []
            for ch, count in stack:
                result.append(ch * count)
            return ''.join(result)

        def dfs(board: str, hand_counter: Counter) -> int:
            if not board:
                return 0
            min_steps = float('inf')
            i = 0
            n = len(board)
            while i < n:
                j = i + 1
                while j < n and board[j] == board[i]:
                    j += 1
                balls_needed = 3 - (j - i)
                ball_color = board[i]
                if hand_counter[ball_color] >= balls_needed:
                    new_hand = hand_counter.copy()
                    new_hand[ball_color] -= balls_needed
                    new_board = clean(board[:i] + board[j:])
                    steps = dfs(new_board, new_hand)
                    if steps >= 0 and steps + balls_needed < min_steps:
                        min_steps = steps + balls_needed
                i = j
            return -1 if min_steps == float('inf') else min_steps

        hand_counter = Counter(hand)
        return dfs(board, hand_counter)