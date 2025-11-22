from collections import Counter, deque

class Solution:
    def minStickers(self, stickers: list[str], target: str) -> int:
        # Convert stickers to list of frequency counters
        stickers_freq = [Counter(s) for s in stickers]
        # Sort stickers by decreasing max frequency of any character
        stickers_freq.sort(key=lambda c: -max(c.values()) if c else 0)

        queue = deque([(target, 0)])
        memo = {target: 0}

        while queue:
            current_target, used_stickers = queue.popleft()

            for sticker in stickers_freq:
                # If first character of current_target not in sticker, skip
                if current_target[0] not in sticker:
                    continue

                remaining = Counter(current_target)
                for ch in sticker:
                    if ch in remaining:
                        remaining[ch] -= sticker[ch]
                        if remaining[ch] <= 0:
                            del remaining[ch]

                new_target = ''.join(sorted(ch * freq for ch, freq in remaining.items()))
                if new_target == '':
                    return used_stickers + 1

                if new_target not in memo:
                    memo[new_target] = used_stickers + 1
                    queue.append((new_target, used_stickers + 1))

        return -1