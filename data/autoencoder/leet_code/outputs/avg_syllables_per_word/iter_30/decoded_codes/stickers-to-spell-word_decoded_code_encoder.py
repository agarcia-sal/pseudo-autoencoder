from collections import Counter, deque

class Solution:
    def minStickers(self, stickers: list[str], target: str) -> int:
        sticker_counters = [Counter(sticker) for sticker in stickers]
        sticker_counters.sort(key=lambda c: -max(c.values()) if c else 0)

        queue = deque([(target, 0)])
        memo = {target: 0}

        while queue:
            current_target, used_stickers = queue.popleft()
            if not current_target:
                return used_stickers
            first_char = current_target[0]
            for sticker_freq in sticker_counters:
                if first_char not in sticker_freq:
                    continue
                remaining_counts = Counter(current_target)
                # Subtract counts but keep only positive counts
                for ch in sticker_freq:
                    remaining_counts[ch] = max(0, remaining_counts[ch] - sticker_freq[ch])
                # Rebuild the target string sorted
                new_target_string = ''.join(sorted(ch * cnt for ch, cnt in remaining_counts.items() if cnt > 0))
                if not new_target_string:
                    return used_stickers + 1
                if new_target_string not in memo:
                    memo[new_target_string] = used_stickers + 1
                    queue.append((new_target_string, used_stickers + 1))
        return -1