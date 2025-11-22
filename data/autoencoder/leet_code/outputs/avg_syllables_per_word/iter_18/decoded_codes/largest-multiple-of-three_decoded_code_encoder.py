from collections import Counter

class Solution:
    def largestMultipleOfThree(self, digits: list[int]) -> str:
        count = self.create_Counter(digits)
        total_sum = self.calculate_Sum(digits)
        remainder = total_sum % 3

        if remainder == 1:
            for d in [1, 4, 7]:
                if count[d] > 0:
                    count[d] -= 1
                    break
            else:
                for d in [2, 5, 8]:
                    if count[d] > 1:
                        count[d] -= 2
                        break

        elif remainder == 2:
            for d in [2, 5, 8]:
                if count[d] > 0:
                    count[d] -= 1
                    break
            else:
                for d in [1, 4, 7]:
                    if count[d] > 1:
                        count[d] -= 2
                        break

        result = []
        for digit in range(9, -1, -1):
            segment = self.replicate_Character(str(digit), count[digit])
            result.append(segment)

        final_number = self.join_Strings(result)

        if not final_number or final_number[0] == '0':
            return '0'
        else:
            return final_number

    # Auxiliary methods as specified/required

    def create_Counter(self, digits: list[int]) -> Counter[int]:
        return Counter(digits)

    def calculate_Sum(self, digits: list[int]) -> int:
        return sum(digits)

    def replicate_Character(self, ch: str, freq: int) -> str:
        return ch * freq

    def join_Strings(self, segments: list[str]) -> str:
        return ''.join(segments)