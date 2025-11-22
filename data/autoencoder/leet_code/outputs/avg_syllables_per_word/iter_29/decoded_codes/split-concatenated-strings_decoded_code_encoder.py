class Solution:
    def splitLoopedString(self, list_of_strings):
        n = len(list_of_strings)
        # Replace each string with its lexicographically maximum between itself and its reversed
        for i in range(n):
            rev = list_of_strings[i][::-1]
            if rev > list_of_strings[i]:
                list_of_strings[i] = rev

        doubled = list_of_strings + list_of_strings
        maximum_string = ""

        for i in range(n):
            for use_reversed in (False, True):
                current = list_of_strings[i][::-1] if use_reversed else list_of_strings[i]

                # Concatenate the strings excluding current one (circularly)
                remaining = "".join(doubled[i + 1:i + n])

                length = len(current)
                for cut in range(length + 1):
                    candidate = current[cut:] + remaining + current[:cut]
                    if candidate > maximum_string:
                        maximum_string = candidate

        return maximum_string