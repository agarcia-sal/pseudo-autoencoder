class Solution:
    def minAbbreviation(self, target: str, dictionary: list[str]) -> str:
        def is_valid_abbr(s: str, abbr: str) -> bool:
            i = 0
            j = 0
            while i < len(s) and j < len(abbr):
                if abbr[j].isdigit():
                    if abbr[j] == '0':  # leading zero not allowed
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

        def generate_abbrs(word: str, length: int, abbr: str = '', index: int = 0, skip_count: int = 0):
            if index == length:
                if skip_count > 0:
                    abbr += str(skip_count)
                abbrs.append(abbr)
                return
            # Option 1: skip current letter (increase skip_count)
            generate_abbrs(word, length, abbr, index + 1, skip_count + 1)
            # Option 2: keep current letter (add skip_count first if any)
            new_abbr = abbr + (str(skip_count) if skip_count > 0 else '') + word[index]
            generate_abbrs(word, length, new_abbr, index + 1, 0)

        def find_unique_abbr() -> str | None:
            for length in range(1, len(target) + 1):
                nonlocal abbrs
                abbrs = []
                generate_abbrs(target, len(target))
                min_abbr = None
                min_length = float('inf')
                for abbr in abbrs:
                    if all(not is_valid_abbr(word, abbr) for word in filtered_dict):
                        if len(abbr) < min_length:
                            min_length = len(abbr)
                            min_abbr = abbr
                if min_abbr is not None:
                    return min_abbr
            return None  # in case no abbreviation found

        filtered_dict = [word for word in dictionary if len(word) == len(target)]
        abbrs = []
        return find_unique_abbr()