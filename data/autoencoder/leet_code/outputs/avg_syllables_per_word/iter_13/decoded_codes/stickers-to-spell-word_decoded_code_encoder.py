from collections import deque, Counter

class Solution:
    def minStickers(self, stickers: list[str], target: str) -> int:
        # Convert each sticker into a frequency count Counter
        sticker_counts = [Counter(sticker) for sticker in stickers]
        # Sort stickers descending by their maximum character count
        sticker_counts.sort(key=lambda c: max(c.values(), default=0), reverse=True)

        queue = deque([(target, 0)])
        memo = {target: 0}

        while queue:
            current_target, used_stickers = queue.popleft()
            current_count = Counter(current_target)

            for sticker in sticker_counts:
                # If the first character of current_target is not in the sticker, skip
                # This matches the pseudocode condition: element at position one of current_target not present in sticker
                if current_target[0] not in sticker:
                    continue

                # Subtract sticker counts to get remaining letters
                remaining = current_count - sticker  # subtract counts, removing negatives automatically
                if not remaining:
                    return used_stickers + 1
                # Construct new_target string from remaining characters sorted
                new_target = ''.join(sorted(remaining.elements()))

                if new_target not in memo:
                    memo[new_target] = used_stickers + 1
                    queue.append((new_target, used_stickers + 1))

        return -1