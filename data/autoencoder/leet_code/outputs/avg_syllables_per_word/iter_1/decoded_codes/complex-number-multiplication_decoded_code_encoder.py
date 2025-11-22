def parse_complex(num):
    parts = num.split('+')
    return int(parts[0]), int(parts[1][:-1])

def multiply_complex(num1, num2):
    real1, imag1 = parse_complex(num1)
    real2, imag2 = parse_complex(num2)
    real = real1 * real2 - imag1 * imag2
    imag = real1 * imag2 + imag1 * real2
    return f"{real}+{imag}i"