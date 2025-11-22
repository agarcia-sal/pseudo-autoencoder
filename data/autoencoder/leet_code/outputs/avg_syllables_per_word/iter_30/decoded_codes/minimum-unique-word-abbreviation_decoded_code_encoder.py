class Solution:
    def minAbbreviation(self, target, dictionary):
        def is_valid_abbr(s, abbr):
            i, j = 0, 0
            while i < len(s) and j < len(abbr):
                if abbr[j].isdigit():
                    if abbr[j] == '0':  # Leading zero in number is invalid
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
            # Abbreviate current character
            generate_abbrs(word, length, abbr, index + 1, skip_count + 1)
            # Keep current character (append skip_count if > 0 first)
            if skip_count > 0:
                abbr += str(skip_count)
            generate_abbrs(word, length, abbr + word[index], index + 1, 0)

        filtered_dict = [word for word in dictionary if len(word) == len(target)]
        abbrs = []

        def find_unique_abbr():
            for length in range(1, len(target) + 1):
                abbrs.clear()
                generate_abbrs(target, len(target), "", 0, 0)
                min_abbr = None
                min_length = float('inf')
                for abbr in abbrs:
                    # Check that abbr is not a valid abbreviation of any word in filtered_dict
                    if all(not is_valid_abbr(word, abbr) for word in filtered_dict):
                        if len(abbr) < min_length:
                            min_length = len(abbr)
                            min_abbr = abbr
                if min_abbr is not None:
                    return min_abbr
            return ""  # In case no unique abbreviation is found, return empty string

        return find_unique_abbr()