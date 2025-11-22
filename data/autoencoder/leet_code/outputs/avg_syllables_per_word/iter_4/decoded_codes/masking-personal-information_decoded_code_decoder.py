import re

class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            local, domain = s.split('@')
            masked_local = local[0] + '*****' + local[-1]
            return (masked_local.lower() + '@' + domain.lower())
        else:
            digits = ''.join(re.findall(r'\d', s))
            local_number = '***-***-' + digits[-4:]
            if len(digits) == 10:
                return local_number
            else:
                country_code_length = len(digits) - 10
                country_code = '+' + ('*' * country_code_length) + '-'
                return country_code + local_number