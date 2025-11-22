from math import gcd

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        lcm = p * q // gcd(p, q)
        vertical_reflections = lcm // p
        horizontal_reflections = lcm // q

        if vertical_reflections % 2 == 0:
            return 0
        elif horizontal_reflections % 2 == 1:
            return 1
        else:
            return 2