class Solution:
    def canWin(self, currentState):
        memo = {}

        def can_win_helper(state):
            if state in memo:
                return memo[state]

            for i in range(len(state) - 1):
                if state[i:i+2] == "++":
                    new_state = state[:i] + "--" + state[i+2:]
                    if not can_win_helper(new_state):
                        memo[state] = True
                        return True

            memo[state] = False
            return False

        return can_win_helper(currentState)