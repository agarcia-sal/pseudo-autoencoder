from collections import Counter, deque

class Solution:
    def minStickers(self, list_of_stickers, target_string) -> int:
        # Preprocess stickers into Counters of character frequencies
        list_of_sticker_counters = [Counter(sticker) for sticker in list_of_stickers]
        # Sort by the maximum character frequency descending to prioritize more impactful stickers
        list_of_sticker_counters.sort(key=lambda c: -max(c.values()) if c else 0)

        processing_queue = deque([(target_string, 0)])
        memoization_table = {target_string: 0}

        while processing_queue:
            current_target_string, number_of_stickers_used = processing_queue.popleft()

            for sticker_counter in list_of_sticker_counters:
                # If the second character of current_target_string is not in sticker, continue
                # Note: pseudocode says "character at position one" (1-based?), so index 1 (0-based) = second char
                # If target string length < 2, index 1 char doesn't exist, skip this check
                if len(current_target_string) < 2 or current_target_string[1] not in sticker_counter:
                    continue

                remaining_characters_counter = Counter(current_target_string)
                for ch in sticker_counter:
                    remaining_characters_counter[ch] -= sticker_counter[ch]
                    if remaining_characters_counter[ch] <= 0:
                        del remaining_characters_counter[ch]

                # Construct new target string from remaining characters sorted ascending
                new_target_string = ''.join(ch * remaining_characters_counter[ch] for ch in sorted(remaining_characters_counter))

                if not new_target_string:
                    return number_of_stickers_used + 1

                if new_target_string not in memoization_table:
                    memoization_table[new_target_string] = number_of_stickers_used + 1
                    processing_queue.append((new_target_string, number_of_stickers_used + 1))

        return -1