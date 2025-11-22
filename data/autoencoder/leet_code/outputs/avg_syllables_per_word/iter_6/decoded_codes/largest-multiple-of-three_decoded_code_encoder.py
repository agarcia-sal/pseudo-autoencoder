class Solution:
    def largestMultipleOfThree(self, digits):
        count = [0]*10
        for d in digits:
            count[d] += 1

        total_sum = sum(d * c for d, c in enumerate(count))
        remainder = total_sum % 3

        def remove_digits(d_list, times=1):
            for d in d_list:
                while count[d] > 0 and times > 0:
                    count[d] -= 1
                    nonlocal times
                    times -= 1

        if remainder == 1:
            for d in [1, 4, 7]:
                if count[d] > 0:
                    count[d] -= 1
                    break
            else:
                to_remove = 2
                for d in [2, 5, 8]:
                    while count[d] > 0 and to_remove > 0:
                        count[d] -= 1
                        to_remove -= 1
                    if to_remove == 0:
                        break

        elif remainder == 2:
            for d in [2, 5, 8]:
                if count[d] > 0:
                    count[d] -= 1
                    break
            else:
                to_remove = 2
                for d in [1, 4, 7]:
                    while count[d] > 0 and to_remove > 0:
                        count[d] -= 1
                        to_remove -= 1
                    if to_remove == 0:
                        break

        result = []
        for d in range(9, -1, -1):
            if count[d] > 0:
                result.append(str(d) * count[d])

        final_number = ''.join(result)
        if final_number and final_number[0] == '0':
            return '0'
        return final_number