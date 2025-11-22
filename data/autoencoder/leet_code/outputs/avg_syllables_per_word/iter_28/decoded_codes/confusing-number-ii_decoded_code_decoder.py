from typing import Dict, List

class Solution:
    def confusingNumberII(self, n: int) -> int:
        rotate_map: Dict[int, int] = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        valid_digits: List[int] = [0, 1, 6, 8, 9]

        def is_confusing(num: int) -> bool:
            original_num = num
            rotated_num = 0
            while num > 0:
                digit = num % 10
                rotated_num = rotated_num * 10 + rotate_map[digit]
                num //= 10
            return rotated_num != original_num

        def count_confusing_numbers(limit: int, current: int) -> int:
            if current > limit:
                return 0
            count = 1 if current != 0 and is_confusing(current) else 0
            for digit in valid_digits:
                new_number = current * 10 + digit
                if new_number == 0:
                    continue
                count += count_confusing_numbers(limit, new_number)
            return count

        return count_confusing_numbers(n, 0)