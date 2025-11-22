class Solution:
    def minAbbreviation(self, target: str, dictionary: list[str]) -> str:
        def is_valid_abbr(string_s: str, abbreviation_abbr: str) -> bool:
            i, j = 0, 0
            while i < len(string_s) and j < len(abbreviation_abbr):
                if abbreviation_abbr[j].isdigit():
                    # Leading zero is invalid
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

        def generate_abbrs(word: str, length_value: int, abbreviation_abbr: str, index_current: int, skip_count_value: int):
            if index_current == length_value:
                if skip_count_value > 0:
                    abbreviation_abbr += str(skip_count_value)
                abbrs.append(abbreviation_abbr)
                return
            # Abbreviate current character (increment skip count)
            generate_abbrs(word, length_value, abbreviation_abbr, index_current + 1, skip_count_value + 1)
            # Keep current character (append skip count if exists, then char, reset skip count)
            if skip_count_value > 0:
                abbreviation_abbr += str(skip_count_value)
            abbreviation_abbr += word[index_current]
            generate_abbrs(word, length_value, abbreviation_abbr, index_current + 1, 0)

        def find_unique_abbr() -> str | None:
            for length_value in range(1, len(target) + 1):
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
            return None

        filtered_dict = [word for word in dictionary if len(word) == len(target)]
        abbrs = []
        return find_unique_abbr()