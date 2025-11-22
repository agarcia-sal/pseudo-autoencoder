class Solution:
    def findReplaceString(self, s: str, indices: list[int], sources: list[str], targets: list[str]) -> str:
        # Combine the inputs and sort by the indices
        replacements = sorted(zip(indices, sources, targets), key=lambda x: x[0])
        result = []
        prev_end = 0
        for index, source, target in replacements:
            # Append the substring between the end of the last replacement and the current index
            result.append(s[prev_end:index])
            # If the source substring matches the original substring at the given index, replace it
            if s.startswith(source, index):
                result.append(target)
                prev_end = index + len(source)
            else:
                result.append(s[index:index+len(source)])
                prev_end = index + len(source)
        # Append the remaining part of the string after the last replacement
        result.append(s[prev_end:])
        return "".join(result)