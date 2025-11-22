from collections import Counter

class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def clean(b: str) -> str:
            stack = []
            for ball in b:
                if stack and stack[-1][0] != ball and stack[-1][1] >= 3:
                    stack.pop()
                if not stack or stack[-1][0] != ball:
                    stack.append([ball, 1])
                else:
                    stack[-1][1] += 1
            if stack and stack[-1][1] >= 3:
                stack.pop()
            return ''.join(ball * count for ball, count in stack)

        def dfs(b: str, hand_count: Counter) -> int:
            if not b:
                return 0
            min_steps = float('inf')
            i = 0
            while i < len(b):
                j = i + 1
                while j < len(b) and b[j] == b[i]:
                    j += 1
                needed = 3 - (j - i)
                if hand_count[b[i]] >= needed:
                    new_hand_count = hand_count.copy()
                    new_hand_count[b[i]] -= needed
                    new_board = clean(b[:i] + b[j:])
                    steps = dfs(new_board, new_hand_count)
                    if steps >= 0:
                        min_steps = min(min_steps, steps + needed)
                i = j
            return min_steps if min_steps != float('inf') else -1

        hand_counter = Counter(hand)
        return dfs(board, hand_counter)