class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        def parse_complex(num):
            real, imag = num.split('+')
            return int(real), int(imag[:-1])

        real1, imag1 = parse_complex(num1)
        real2, imag2 = parse_complex(num2)

        real_part = real1 * real2 - imag1 * imag2
        imaginary_part = real1 * imag2 + imag1 * real2

        return f"{real_part}+{imaginary_part}i"