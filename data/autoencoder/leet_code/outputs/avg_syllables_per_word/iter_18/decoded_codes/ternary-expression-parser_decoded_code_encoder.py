class Solution:
    def parseTernary(self, expression: str) -> str:
        def evaluate(index: int):
            # If the next character is ':' or this is the last character, return this character and next index
            if index == len(expression) - 1 or expression[index + 1] == ':':
                return expression[index], index + 2
            # Evaluate the true part starting after 'T?' or 'F?'
            true_part, next_index = evaluate(index + 2)
            # Evaluate the false part starting after the true part
            false_part, final_index = evaluate(next_index)
            # Return based on current condition character
            if expression[index] == 'T':
                return true_part, final_index
            else:
                return false_part, final_index

        result, _ = evaluate(0)
        return result