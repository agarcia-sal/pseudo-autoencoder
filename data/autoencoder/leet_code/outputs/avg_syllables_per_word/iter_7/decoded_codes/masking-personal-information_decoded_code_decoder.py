from typing import List

class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            local, domain = s.split('@')
            masked_local = local[0].lower() + "*****" + local[-1].lower()
            return masked_local + '@' + domain.lower()
        else:
            digits = [c for c in s if c.isdigit()]
            local_number = "***-***-" + "".join(digits[-4:])
            if len(digits) == 10:
                return local_number
            else:
                country_code_length = len(digits) - 10
                country_code = "+" + ("*" * country_code_length) + "-"
                return country_code + local_number