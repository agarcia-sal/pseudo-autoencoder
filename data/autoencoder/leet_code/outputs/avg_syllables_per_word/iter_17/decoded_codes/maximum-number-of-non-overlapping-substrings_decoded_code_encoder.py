class Solution:
    def maxNumOfSubstrings(self, string_s: str) -> list[str]:
        dictionary_first = {}
        dictionary_last = {}
        for i, c in enumerate(string_s):
            if c not in dictionary_first:
                dictionary_first[c] = i
            dictionary_last[c] = i

        list_intervals = []
        for c in dictionary_first:
            start = dictionary_first[c]
            end = dictionary_last[c]
            i = start
            while i <= end:
                if dictionary_first[string_s[i]] < start:
                    break
                end = max(end, dictionary_last[string_s[i]])
                i += 1
            if i > end:
                list_intervals.append((start, end))

        list_intervals.sort(key=lambda x: x[1])

        list_result = []
        prev_end = -1
        for start, end in list_intervals:
            if start > prev_end:
                list_result.append(string_s[start:end + 1])
                prev_end = end

        return list_result