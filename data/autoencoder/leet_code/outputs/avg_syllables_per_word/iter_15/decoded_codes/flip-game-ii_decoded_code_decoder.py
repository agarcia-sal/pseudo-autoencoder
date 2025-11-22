from typing import Dict

class Solution:
    def canWin(self, currentState: str) -> bool:
        memo: Dict[str, bool] = {}

        def can_win_helper(state: str) -> bool:
            if state in memo:
                return memo[state]
            length_of_state = len(state)
            for index in range(length_of_state - 1):
                substring_at_index = state[index:index+2]
                if substring_at_index == "++":
                    new_state = state[:index] + "--" + state[index+2:]
                    opponent_can_win = can_win_helper(new_state)
                    if not opponent_can_win:
                        memo[state] = True
                        return True
            memo[state] = False
            return False

        return can_win_helper(currentState)