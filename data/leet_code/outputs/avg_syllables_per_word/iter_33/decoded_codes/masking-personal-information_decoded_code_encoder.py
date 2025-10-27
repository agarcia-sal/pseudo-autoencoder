class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            at_idx = s.index('@')
            local_part = s[:at_idx]
            domain_part = s[at_idx+1:]
            masked_local_part = local_part[0] + '*****' + local_part[-1]
            return masked_local_part.lower() + '@' + domain_part.lower()
        else:
            digits_only = ''.join(c for c in s if c.isdigit())
            local_number_mask = '***-***-' + digits_only[-4:]
            if len(digits_only) == 10:
                return local_number_mask
            else:
                country_code_length = len(digits_only) - 10
                country_code_mask = '+' + ('*' * country_code_length) + '-'
                return country_code_mask + local_number_mask