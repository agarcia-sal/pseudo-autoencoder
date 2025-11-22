from typing import List

class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        # Precomputed ratios corresponding to:
        # 1/9, 1/99, 1/999, 1/9999
        ratios: List[float] = [
            1 / 9,
            1 / 99,
            1 / 999,
            1 / 9999,
        ]

        def valueOf(s: str) -> float:
            open_paren_index = s.find('(')
            if open_paren_index == -1:
                # No repeating decimal
                try:
                    return float(s)
                except ValueError:
                    return 0.0  # Graceful fallback if input malformed

            close_paren_index = s.find(')')
            dot_index = s.find('.')

            # Parse integer and non-repeating decimal part as float
            # substring from start to (open_paren_index - 1) inclusive
            # e.g. "0.1(6)" open_paren_index=3, so substring s[:2] = "0.1"
            integer_and_non_repeating_str = s[:open_paren_index]
            try:
                integer_and_non_repeating = float(integer_and_non_repeating_str)
            except ValueError:
                integer_and_non_repeating = 0.0  # fallback

            non_repeating_length = open_paren_index - dot_index - 1

            # Extract repeating digits as integer
            # substring from (open_paren_index + 1) to (close_paren_index)
            repeating_str = s[open_paren_index + 1:close_paren_index]
            try:
                repeating = int(repeating_str)
            except ValueError:
                repeating = 0  # fallback

            repeating_length = close_paren_index - open_paren_index - 1

            # Safety check for repeating_length in ratios range
            if 1 <= repeating_length <= len(ratios):
                ratio = ratios[repeating_length - 1]
            else:
                # For longer repeating parts beyond precomputed ratios,
                # use the formula: 1 / (10^repeating_length - 1)
                ratio = 1 / (10 ** repeating_length - 1)

            return integer_and_non_repeating + repeating * (10 ** (-non_repeating_length)) * ratio

        return abs(valueOf(s) - valueOf(t)) < 1e-9