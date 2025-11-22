class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            local, domain = self.split_email(s)
            masked_local = local[0] + ('*' * 5) + local[-1]
            return masked_local.lower() + '@' + domain.lower()
        else:
            digits = self.filter_digits(s)
            local_number = '***-***-' + digits[-4:]
            if len(digits) == 10:
                return local_number
            else:
                country_code_length = len(digits) - 10
                country_code = '+' + ('*' * country_code_length) + '-'
                return country_code + local_number

    def split_email(self, email: str) -> tuple[str, str]:
        local, domain = email.split('@', 1)
        return local, domain

    def filter_digits(self, text: str) -> str:
        return ''.join(ch for ch in text if ch.isdigit())