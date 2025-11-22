class Solution:
    def parseTernary(self, expression: str) -> str:
        def evaluate(index):
            # If the next character is not '?' (or we are at the last character),
            # return the current character and the next index to read from
            if index == len(expression) - 1 or expression[index + 1] == ':':
                return expression[index], index + 1
            # Evaluate the true part (expression after '?')
            true_part, next_index = evaluate(index + 2)
            # Evaluate the false part (expression after ':')
            false_part, final_index = evaluate(next_index)
            # If current character is 'T', choose true_part, else false_part
            if expression[index] == 'T':
                return true_part, final_index
            else:
                return false_part, final_index

        result, _ = evaluate(0)
        return result