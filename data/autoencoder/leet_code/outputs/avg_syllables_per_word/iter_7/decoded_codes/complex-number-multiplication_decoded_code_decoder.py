from typing import Tuple

class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        def parse_complex(num: str) -> Tuple[int, int]:
            parts = num.split('+')
            real = int(parts[0])
            imaginary = int(parts[1][:-1])
            return real, imaginary

        real1, imag1 = parse_complex(num1)
        real2, imag2 = parse_complex(num2)

        real_part = real1 * real2 - imag1 * imag2
        imaginary_part = real1 * imag2 + imag1 * real2

        return f"{real_part}+{imaginary_part}i"