class Solution:
    def largestMultipleOfThree(self, digits):
        count = [0] * 10
        for d in digits:
            count[d] += 1

        total_sum = sum(d * count[d] for d in range(10))
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
        for d in range(9, -1, -1):
            if count[d] > 0:
                result.append(str(d) * count[d])

        final_number = ''.join(result)

        if final_number == '' or final_number[0] == '0':
            return '0'
        else:
            return final_number