from math import gcd

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        gcd_value = gcd(p, q)
        lcm = (p * q) // gcd_value
        vertical_reflections = lcm // p
        horizontal_reflections = lcm // q
        if vertical_reflections % 2 == 0:
            return 0
        elif horizontal_reflections % 2 == 1:
            return 1
        else:
            return 2