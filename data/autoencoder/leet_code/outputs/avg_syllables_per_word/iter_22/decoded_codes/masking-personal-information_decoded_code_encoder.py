class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            local, domain = s.split('@', 1)
            masked_local = local[0].lower() + "*****" + local[-1].lower()
            return masked_local + "@" + domain.lower()
        else:
            digits = ''.join(ch for ch in s if ch.isdigit())
            local_number = "***-***-" + digits[-4:]
            if len(digits) == 10:
                return local_number
            else:
                country_code_length = len(digits) - 10
                country_code = "+" + ("*" * country_code_length) + "-"
                return country_code + local_number