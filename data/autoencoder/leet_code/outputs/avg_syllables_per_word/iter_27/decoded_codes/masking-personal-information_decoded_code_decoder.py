class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            local, domain = s.split('@', 1)
            masked_local = local[0] + '*****' + local[-1]
            return masked_local.lower() + '@' + domain.lower()
        else:
            digits = ''.join(ch for ch in s if ch.isdigit())
            last_four = digits[-4:]
            local_number = '***-***-' + last_four
            if len(digits) == 10:
                return local_number
            else:
                country_len = len(digits) - 10
                country_code = '+' + ('*' * country_len) + '-'
                return country_code + local_number