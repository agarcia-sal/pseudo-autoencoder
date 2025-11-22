class Solution:
    def customSortString(self, order: str, s: str) -> str:
        pos = {ch: i + 1 for i, ch in enumerate(order)}  # Use i+1 so that characters not in order get 0 by default
        return ''.join(sorted(s, key=lambda ch: pos.get(ch, 0)))