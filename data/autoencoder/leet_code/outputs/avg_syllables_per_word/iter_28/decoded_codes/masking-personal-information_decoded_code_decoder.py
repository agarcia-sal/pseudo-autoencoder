import re

class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            at_pos = s.index('@')
            local = s[:at_pos]
            domain = s[at_pos+1:]
            masked_local = (local[0].lower() + "*****" + local[-1].lower())
            return masked_local + "@" + domain.lower()
        else:
            digits = re.sub(r'\D', '', s)
            length = len(digits)
            local_mask = "***-***-" + digits[-4:]
            if length == 10:
                return local_mask
            else:
                country_code_len = length - 10
                country_code_mask = "+" + "*" * country_code_len + "-"
                return country_code_mask + local_mask