class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        def parse_complex(num: str):
            # split at '+'
            parts = num.split('+')
            real = int(parts[0])
            # remove trailing 'i' from imaginary part
            imaginary = int(parts[1][:-1])
            return real, imaginary

        real1, imag1 = parse_complex(num1)
        real2, imag2 = parse_complex(num2)

        real_part = real1 * real2 - imag1 * imag2
        imaginary_part = real1 * imag2 + imag1 * real2

        return str(real_part) + '+' + str(imaginary_part) + 'i'