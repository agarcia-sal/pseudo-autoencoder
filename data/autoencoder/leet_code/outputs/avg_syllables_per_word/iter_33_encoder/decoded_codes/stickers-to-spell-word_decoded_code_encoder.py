from collections import Counter, deque

class Solution:
    def minStickers(self, stickers, target):
        # Convert each sticker into a Counter of character counts
        stickers = [Counter(sticker) for sticker in stickers]
        # Sort stickers by the negation of the maximum character count (descending)
        stickers.sort(key=lambda c: max(c.values()) if c else 0, reverse=True)

        queue = deque([(target, 0)])
        memo = {target: 0}

        while queue:
            current_target, used_stickers = queue.popleft()
            first_char = current_target[0] if current_target else ''

            for sticker in stickers:
                if first_char not in sticker:
                    continue

                # Count characters in current_target
                target_count = Counter(current_target)
                # Subtract counts from the sticker
                remaining = target_count - sticker

                # Build new target string by repeating chars according to remaining counts, sorted
                new_target = ''.join(sorted(char * count for char, count in remaining.items()))

                if len(new_target) == 0:
                    return used_stickers + 1

                if new_target not in memo:
                    memo[new_target] = used_stickers + 1
                    queue.append((new_target, used_stickers + 1))

        return -1