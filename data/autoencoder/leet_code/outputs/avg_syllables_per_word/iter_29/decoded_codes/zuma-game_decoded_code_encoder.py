from collections import Counter

class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def clean(board_string: str) -> str:
            stack = []
            for ball in board_string:
                # Remove sequences of 3 or more different balls before processing the current ball
                while stack and stack[-1][1] >= 3 and stack[-1][0] != ball:
                    stack.pop()
                if not stack or stack[-1][0] != ball:
                    stack.append([ball, 1])
                else:
                    stack[-1][1] += 1
            # Remove any trailing sequences of 3 or more balls
            while stack and stack[-1][1] >= 3:
                stack.pop()
            # Rebuild the cleaned board string
            return ''.join(ball * count for ball, count in stack)

        def dfs(current_board: str, current_hand_counter: Counter) -> int:
            if not current_board:
                return 0  # Board cleared

            min_steps = float('inf')
            i = 0
            length = len(current_board)

            while i < length:
                j = i + 1
                while j < length and current_board[j] == current_board[i]:
                    j += 1
                # Balls needed to remove this group (at least 3)
                need = 3 - (j - i)
                ball = current_board[i]

                if current_hand_counter[ball] >= need:
                    # If need is <= 0, it means the group already >= 3, so 0 balls needed
                    need = max(need, 0)
                    new_hand = current_hand_counter.copy()
                    new_hand[ball] -= need
                    new_board = clean(current_board[:i] + current_board[j:])
                    res = dfs(new_board, new_hand)
                    if res >= 0:
                        min_steps = min(min_steps, res + need)
                i = j

            return -1 if min_steps == float('inf') else min_steps

        hand_counter = Counter(hand)
        return dfs(board, hand_counter)