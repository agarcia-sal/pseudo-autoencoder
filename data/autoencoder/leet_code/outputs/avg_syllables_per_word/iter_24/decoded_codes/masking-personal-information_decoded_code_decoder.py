class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            local, domain = s.split('@', 1)
            first_character = local[0]
            last_character = local[-1]
            five_asterisks = '*****'
            masked_local = first_character + five_asterisks + last_character
            lowercase_masked_local = masked_local.lower()
            lowercase_domain = domain.lower()
            return lowercase_masked_local + '@' + lowercase_domain
        else:
            digits = ''.join(ch for ch in s if ch.isdigit())
            last_four_digits = digits[-4:]
            local_number = '***-***-' + last_four_digits
            if len(digits) == 10:
                return local_number
            else:
                country_code_length = len(digits) - 10
                country_code = '+' + ('*' * country_code_length) + '-'
                return country_code + local_number