class Solution:
    def canWin(self, currentState: str) -> bool:
        memo = {}

        def can_win_helper(state: str) -> bool:
            if state in memo:
                return memo[state]

            for i in range(len(state) - 1):
                if state[i] == '+' and state[i + 1] == '+':
                    new_state = state[:i] + '--' + state[i + 2:]
                    if not can_win_helper(new_state):
                        memo[state] = True
                        return True

            memo[state] = False
            return False

        return can_win_helper(currentState)