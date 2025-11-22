from collections import Counter

class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def clean(board: str) -> str:
            stack = []
            for ball in board:
                # Remove groups of 3 or more consecutive balls of different color before adding new ball
                while stack and stack[-1][0] != ball and stack[-1][1] >= 3:
                    stack.pop()
                if not stack or stack[-1][0] != ball:
                    stack.append([ball, 1])
                else:
                    stack[-1][1] += 1
            # Final check for last group
            if stack and stack[-1][1] >= 3:
                stack.pop()
            result = []
            for ball, count in stack:
                result.append(ball * count)
            return ''.join(result)

        def dfs(board: str, hand_counter: Counter) -> int:
            if not board:
                return 0
            min_steps = float('inf')
            i = 0
            while i < len(board):
                j = i + 1
                while j < len(board) and board[j] == board[i]:
                    j += 1
                balls_needed = 3 - (j - i)
                if balls_needed > 0 and hand_counter[board[i]] >= balls_needed:
                    new_hand_counter = hand_counter.copy()
                    new_hand_counter[board[i]] -= balls_needed
                    # Remove used balls from hand counter if count reaches zero
                    if new_hand_counter[board[i]] == 0:
                        del new_hand_counter[board[i]]
                    new_board = clean(board[:i] + board[j:])
                    steps = dfs(new_board, new_hand_counter)
                    if steps >= 0:
                        min_steps = min(min_steps, steps + balls_needed)
                i = j
            return min_steps if min_steps != float('inf') else -1

        hand_counter = Counter(hand)
        return dfs(board, hand_counter)