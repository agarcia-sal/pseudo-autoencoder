from collections import Counter

class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def clean(board: str) -> str:
            stack = []
            for ball in board:
                # Remove sequences of three or more balls of different color before adding new ball
                while stack and stack[-1][0] != ball and stack[-1][1] >= 3:
                    stack.pop()
                if not stack or stack[-1][0] != ball:
                    stack.append([ball, 1])
                else:
                    stack[-1][1] += 1
            # After processing all, remove trailing sequences of three or more
            while stack and stack[-1][1] >= 3:
                stack.pop()
            return ''.join(char * count for char, count in stack)

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
                needed = 3 - (j - i)
                if hand_counter[board[i]] >= needed:
                    new_hand = hand_counter.copy()
                    new_hand[board[i]] -= needed
                    # Construct new board after removing the sequence
                    new_board = clean(board[:i] + board[j:])
                    steps = dfs(new_board, new_hand)
                    if steps >= 0:
                        min_steps = min(min_steps, steps + needed)
                i = j
            return min_steps if min_steps != float('inf') else -1

        hand_counter = Counter(hand)
        return dfs(board, hand_counter)