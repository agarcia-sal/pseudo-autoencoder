from typing import Dict

class Solution:
    def canWin(self, currentState: str) -> bool:
        memo: Dict[str, bool] = {}

        def can_win_helper(state: str) -> bool:
            if state in memo:
                return memo[state]

            for i in range(len(state) - 1):
                # Check if two consecutive '+' exist starting at index i
                if state[i:i+2] == "++":
                    # Flip "++" to "--" at position i
                    new_state = state[:i] + "--" + state[i+2:]
                    # If opponent cannot win from new_state, current player wins
                    if not can_win_helper(new_state):
                        memo[state] = True
                        return True

            memo[state] = False
            return False

        return can_win_helper(currentState)