class Solution:
    def minAbbreviation(self, target, dictionary):
        # Helper function to check if abbr is a valid abbreviation of s
        def is_valid_abbr(s, abbr):
            i = 0  # index for s
            j = 0  # index for abbr
            while i < len(s) and j < len(abbr):
                if abbr[j].isdigit():
                    # leading zero is not allowed
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

        # Generate all abbreviations of the word using backtracking
        def generate_abbrs(word, length, abbr, index, skip_count):
            if index == length:
                if skip_count > 0:
                    abbr += str(skip_count)
                abbrs.append(abbr)
                return
            # Option 1: skip current character
            generate_abbrs(word, length, abbr, index + 1, skip_count + 1)
            # Option 2: keep current character
            next_abbr = abbr
            if skip_count > 0:
                next_abbr += str(skip_count)
            next_abbr += word[index]
            generate_abbrs(word, length, next_abbr, index + 1, 0)

        # Find the minimal unique abbreviation that doesn't match any word in filtered_dict
        def find_unique_abbr():
            for length in range(1, len(target) + 1):
                abbrs.clear()
                generate_abbrs(target, len(target), "", 0, 0)
                min_abbr = None
                min_length = float("inf")
                for abbr in abbrs:
                    # If no word in filtered_dict matches this abbreviation
                    if all(not is_valid_abbr(word, abbr) for word in filtered_dict):
                        if len(abbr) < min_length:
                            min_length = len(abbr)
                            min_abbr = abbr
                if min_abbr is not None:
                    return min_abbr
            return ""  # In case no abbreviation found; problem doesn't specify but safe fallback

        filtered_dict = [word for word in dictionary if len(word) == len(target)]
        abbrs = []
        return find_unique_abbr()