class Solution:
    def minAbbreviation(self, target, dictionary):
        def is_valid_abbr(s, abbr):
            i = 0
            j = 0
            while i < len(s) and j < len(abbr):
                if abbr[j].isdigit():
                    if abbr[j] == '0':  # leading zero invalid
                        return False
                    shift = 0
                    while j < len(abbr) and abbr[j].isdigit():
                        shift = shift * 10 + int(abbr[j])
                        j += 1
                    i += shift
                else:
                    if i >= len(s) or s[i] != abbr[j]:
                        return False
                    i += 1
                    j += 1
            return i == len(s) and j == len(abbr)

        def generate_abbrs(word, length, abbr='', index=0, skip_count=0):
            if index == length:
                if skip_count > 0:
                    abbr += str(skip_count)
                abbrs.append(abbr)
                return
            generate_abbrs(word, length, abbr, index + 1, skip_count + 1)
            next_abbr = abbr
            if skip_count > 0:
                next_abbr += str(skip_count)
            next_abbr += word[index]
            generate_abbrs(word, length, next_abbr, index + 1, 0)

        filtered_dict = [w for w in dictionary if len(w) == len(target)]
        abbrs = []

        def find_unique_abbr():
            for length in range(1, len(target) + 1):
                abbrs.clear()
                generate_abbrs(target, len(target))
                min_abbr = None
                min_length = float('inf')
                for abbr in abbrs:
                    is_unique = True
                    for word in filtered_dict:
                        if is_valid_abbr(word, abbr):
                            is_unique = False
                            break
                    if is_unique and len(abbr) < min_length:
                        min_length = len(abbr)
                        min_abbr = abbr
                if min_abbr is not None:
                    return min_abbr

        return find_unique_abbr()