class Solution:
    def splitLoopedString(self, list_of_strings):
        for i in range(len(list_of_strings)):
            reversed_string = list_of_strings[i][::-1]
            if reversed_string > list_of_strings[i]:
                list_of_strings[i] = reversed_string

        doubled_list_of_strings = list_of_strings + list_of_strings
        max_string = ""

        n = len(list_of_strings)
        for i in range(n):
            for reversed_flag in [False, True]:
                current_string = list_of_strings[i][::-1] if reversed_flag else list_of_strings[i]
                remaining_string = "".join(doubled_list_of_strings[i+1:i+n])
                L = len(current_string)
                for cut_pos in range(L+1):
                    candidate_string = current_string[cut_pos:] + remaining_string + current_string[:cut_pos]
                    if candidate_string > max_string:
                        max_string = candidate_string

        return max_string