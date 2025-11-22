class Solution:
    def findReplaceString(self, s, indices, sources, targets):
        list_of_replacements = sorted(zip(indices, sources, targets), key=lambda x: x[0])
        result_list = []
        previous_end_index = 0
        for current_index, current_source, current_target in list_of_replacements:
            # Append substring between previous end and current index
            if current_index > previous_end_index:
                result_list.append(s[previous_end_index:current_index])
            # Check if source matches substring at current index
            end_index = current_index + len(current_source)
            if s[current_index:end_index] == current_source:
                result_list.append(current_target)
                previous_end_index = end_index
            else:
                # If no match, append the original substring
                result_list.append(s[current_index:end_index])
                previous_end_index = end_index
        # Append any remaining substring after last replacement
        if previous_end_index < len(s):
            result_list.append(s[previous_end_index:])
        return ''.join(result_list)