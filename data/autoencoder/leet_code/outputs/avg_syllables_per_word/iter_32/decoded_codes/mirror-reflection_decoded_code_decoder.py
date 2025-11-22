from math import gcd

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        greatest_common_divisor = gcd(p, q)
        least_common_multiple = p * q // greatest_common_divisor

        vertical_reflections = least_common_multiple // p
        horizontal_reflections = least_common_multiple // q

        if vertical_reflections % 2 == 0:
            return 0
        elif horizontal_reflections % 2 == 1:
            return 1
        else:
            return 2