class Solution:
    def minAbbreviation(self, target, dictionary):
        def is_valid_abbr(s, abbr):
            i, j = 0, 0
            while i < len(s) and j < len(abbr):
                if abbr[j].isdigit():
                    if abbr[j] == '0':
                        return False
                    shift = 0
                    while j < len(abbr) and abbr[j].isdigit():
                        shift = shift * 10 + int(abbr[j])
                        j += 1
                    i += shift
                else:
                    if s[i] != abbr[j]:
                        return False
                    i += 1
                    j += 1
            return i == len(s) and j == len(abbr)

        def generate_abbrs(word, length, abbr, index, skip_count):
            if index == length:
                if skip_count > 0:
                    abbr += str(skip_count)
                abbrs.append(abbr)
                return
            # Option 1: skip current character (increase skip_count)
            generate_abbrs(word, length, abbr, index + 1, skip_count + 1)
            # Option 2: keep current character (append skip_count if any before adding char)
            new_abbr = abbr
            if skip_count > 0:
                new_abbr += str(skip_count)
            new_abbr += word[index]
            generate_abbrs(word, length, new_abbr, index + 1, 0)

        def find_unique_abbr():
            for length in range(1, len(target) + 1):
                abbrs.clear()
                generate_abbrs(target, len(target), '', 0, 0)
                min_abbr = None
                min_length = float('inf')
                for abbr in abbrs:
                    if all(not is_valid_abbr(word, abbr) for word in filtered_dict):
                        if len(abbr) < min_length:
                            min_length = len(abbr)
                            min_abbr = abbr
                if min_abbr is not None:
                    return min_abbr

        filtered_dict = [word for word in dictionary if len(word) == len(target)]
        abbrs = []
        return find_unique_abbr()