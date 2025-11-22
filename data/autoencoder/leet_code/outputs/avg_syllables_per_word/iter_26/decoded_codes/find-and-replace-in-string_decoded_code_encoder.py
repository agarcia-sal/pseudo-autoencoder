class Solution:
    def findReplaceString(self, s: str, indices: list[int], sources: list[str], targets: list[str]) -> str:
        # Combine and sort replacements by starting indices
        replacements = sorted(zip(indices, sources, targets), key=lambda x: x[0])

        result = []
        prev_end = 0

        for index, source, target in replacements:
            # Append substring from prev_end to index
            result.append(s[prev_end:index])
            source_len = len(source)
            # Check if source matches the substring at index
            if s[index:index + source_len] == source:
                result.append(target)
                prev_end = index + source_len
            else:
                # If no match, append the original substring
                result.append(s[index:index + source_len])
                prev_end = index + source_len

        # Append the remaining part of the string after the last replacement
        result.append(s[prev_end:])

        return "".join(result)