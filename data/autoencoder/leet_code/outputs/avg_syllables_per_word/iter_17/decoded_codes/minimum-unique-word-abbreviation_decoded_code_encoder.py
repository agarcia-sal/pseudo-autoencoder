class Solution:
    def minAbbreviation(self, target, dictionary):
        def is_valid_abbr(string_s, abbreviation_abbr):
            i, j = 0, 0
            while i < len(string_s) and j < len(abbreviation_abbr):
                if abbreviation_abbr[j].isdigit():
                    if abbreviation_abbr[j] == '0':
                        return False
                    shift = 0
                    while j < len(abbreviation_abbr) and abbreviation_abbr[j].isdigit():
                        shift = shift * 10 + int(abbreviation_abbr[j])
                        j += 1
                    i += shift
                else:
                    if string_s[i] != abbreviation_abbr[j]:
                        return False
                    i += 1
                    j += 1
            return i == len(string_s) and j == len(abbreviation_abbr)

        def generate_abbrs(word, length, abbr_str, index, skipped):
            if index == length:
                if skipped > 0:
                    abbr_str += str(skipped)
                abbrs.append(abbr_str)
                return
            # Option 1: skip current character (increase skipped count)
            generate_abbrs(word, length, abbr_str, index + 1, skipped + 1)
            # Option 2: keep current character (append skipped count if any, then char)
            if skipped > 0:
                abbr_str += str(skipped)
            generate_abbrs(word, length, abbr_str + word[index], index + 1, 0)

        def FilterWordsByLength(dic, length):
            return [w for w in dic if len(w) == length]

        filtered_dict = FilterWordsByLength(dictionary, len(target))
        abbrs = []

        def find_unique_abbr():
            for abbr_len in range(1, len(target) + 1):
                abbrs.clear()
                generate_abbrs(target, len(target), "", 0, 0)
                min_abbr = None
                min_len = float('inf')
                for abbr in abbrs:
                    # check abbreviation uniqueness
                    if all(not is_valid_abbr(word, abbr) for word in filtered_dict):
                        if len(abbr) < min_len:
                            min_len = len(abbr)
                            min_abbr = abbr
                if min_abbr is not None:
                    return min_abbr
            return ""  # fallback in case no abbreviation found

        return find_unique_abbr()