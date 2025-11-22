class Solution:
    def ambiguousCoordinates(self, s: str) -> list[str]:
        def make(frag: str) -> list[str]:
            n = len(frag)
            res = []
            # Try all possible splits to insert a decimal point or none
            for d in range(1, n + 1):
                left = frag[:d]
                right = frag[d:]
                # Check left part validity: no leading zeros unless single zero
                if (left == "0" or not left.startswith("0")):
                    # Check right part validity: if present, no trailing zeros
                    if not right or not right.endswith("0"):
                        if right:
                            res.append(left + "." + right)
                        else:
                            res.append(left)
            return res

        s = s[1:-1]  # remove surrounding parentheses
        n = len(s)
        ans = []
        for i in range(1, n):
            left_frag = s[:i]
            right_frag = s[i:]
            left_parts = make(left_frag)
            right_parts = make(right_frag)
            for a in left_parts:
                for b in right_parts:
                    ans.append(f"({a}, {b})")
        return ans