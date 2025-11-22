from collections import Counter, deque

class Solution:
    def minStickers(self, list_of_stickers: list[str], target_string: str) -> int:
        stickers = [Counter(sticker) for sticker in list_of_stickers]
        # Sort stickers by negative max frequency of characters (descending order)
        stickers.sort(key=lambda c: -max(c.values()))

        queue = deque([(target_string, 0)])
        memo = {target_string: 0}

        while queue:
            current_target, used_stickers = queue.popleft()

            for sticker in stickers:
                if current_target[0] not in sticker:
                    continue
                remaining = Counter(current_target)
                remaining.subtract(sticker)
                # Remove negative and zero counts from remaining
                new_target = ''.join(sorted(ch * cnt for ch, cnt in remaining.items() if cnt > 0))
                if not new_target:
                    return used_stickers + 1
                if new_target not in memo:
                    memo[new_target] = used_stickers + 1
                    queue.append((new_target, used_stickers + 1))
        return -1