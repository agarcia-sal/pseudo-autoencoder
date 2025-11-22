from collections import Counter, deque

class Solution:
    def minStickers(self, stickers, target):
        # Convert each sticker into a frequency Counter
        stickers = [Counter(sticker) for sticker in stickers]
        # Sort stickers by the highest frequency count of any character descending
        stickers.sort(key=lambda c: -max(c.values()) if c else 0)

        queue = deque([(target, 0)])
        memo = {target: 0}

        while queue:
            current_target, used_stickers = queue.popleft()
            for sticker in stickers:
                # If the first character of current_target is not in this sticker, skip
                if current_target[0] not in sticker:
                    continue

                remaining = Counter(current_target)
                # Subtract sticker counts from remaining target counts
                remaining.subtract(sticker)
                # Remove all zero or negative counts
                new_target_chars = [ch * count for ch, count in remaining.items() if count > 0]
                # Create the new target string sorted lexicographically
                new_target = ''.join(sorted(''.join(new_target_chars)))

                if not new_target:
                    return used_stickers + 1

                if new_target not in memo:
                    memo[new_target] = used_stickers + 1
                    queue.append((new_target, used_stickers + 1))

        return -1