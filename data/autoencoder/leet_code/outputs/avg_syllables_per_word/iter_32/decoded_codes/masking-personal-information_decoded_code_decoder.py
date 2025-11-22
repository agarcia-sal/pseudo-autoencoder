import re

class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            at_index = s.index('@')
            local = s[:at_index]
            domain = s[at_index+1:]
            # Mask local name except first and last character with 5 asterisks
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