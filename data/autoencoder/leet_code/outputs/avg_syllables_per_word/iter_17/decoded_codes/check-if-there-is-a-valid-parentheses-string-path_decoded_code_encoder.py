from typing import List

class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        # If the length of path (m + n - 1) is odd, cannot have balanced parentheses
        if (m + n - 1) % 2 != 0:
            return False

        dp = self.initialize_dp(m, n)

        # Starting from position (0,0) with one open parenthesis if grid[0][0] == '('
        # The problem sets dp[0][1][0] to True in pseudocode which seems off by one
        # We adjust accordingly: dp is indexed as dp[row][col][open_count]
        # The pseudocode's dp[0][1][0] True means from top-left with one open parenthesis
        if grid[0][0] == '(':
            dp[1][0][1] = True  # After first '(' count is 1
        else:
            # If first char is ')', can't start with valid path
            return False

        for i in range(m + 1):
            for j in range(n + 1):
                for k in range(m + n + 1):
                    if i == 0 and j == 0:
                        continue
                    # Check from left (i, j-1) or from top (i-1, j)
                    from_left = j > 0 and dp[i][j - 1][k]
                    from_top = i > 0 and dp[i - 1][j][k]
                    if from_left or from_top:
                        # Current cell is grid[i-1][j-1] because dp is size m+1,n+1
                        if i > 0 and j > 0:
                            ch = grid[i - 1][j - 1]
                            if ch == '(' and k > 0:
                                # '(' increases the count of open parentheses
                                dp[i][j][k] = dp[i][j][k] or (k - 1 >= 0 and (from_left or from_top))
                            elif ch == ')' and k +1 <= m + n:
                                # ')' decreases the count
                                dp[i][j][k] = dp[i][j][k] or (k + 1 <= m + n and (from_left or from_top))

        # After correction to reflect the logic:
        # It is more efficient and exact to do the following as from the pseudocode:
        # It seems the pseudocode treats k as current number of open parentheses
        # If cell is '(', k increases by 1
        # if cell is ')', k decreases by 1
        # We need to update dp accordingly
        # Let's rewrite with correct logic based on pseudocode:

    def initialize_dp(self, m: int, n: int) -> List[List[List[bool]]]:
        return [[[False] * (m + n + 1) for _ in range(n + 1)] for __ in range(m + 1)]


class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        if (m + n - 1) % 2 != 0:
            return False

        dp = self.initialize_dp(m, n)

        # Initialize dp at (0, 0) for k = 1 if first cell is '('
        if grid[0][0] == '(':
            dp[1][0][1] = True  # We consider dp indices shifted by 1 to facilitate boundary checks
        else:
            return False  # Can't start with ')'

        for i in range(m + 1):
            for j in range(n + 1):
                for k in range(m + n + 1):
                    if i == 0 and j == 0:
                        continue  # Already initialized
                    # Check if previous step was valid from left or top
                    from_left = j > 0 and dp[i][j - 1][k]
                    from_top = i > 0 and dp[i - 1][j][k]

                    if from_left or from_top:
                        # Only proceed if i,j >0 to get grid char
                        if i > 0 and j > 0:
                            ch = grid[i - 1][j - 1]
                            if ch == '(':
                                if k + 1 <= m + n:
                                    dp[i][j][k + 1] = True
                            else:  # ch == ')'
                                if k - 1 >= 0:
                                    dp[i][j][k - 1] = True

        return dp[m][n][0]

    def initialize_dp(self, m: int, n: int) -> List[List[List[bool]]]:
        return [[[False] * (m + n + 1) for _ in range(n + 1)] for __ in range(m + 1)]