class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            local, domain = s.split('@')
            masked_local = local[0] + '*****' + local[-1]
            return (masked_local + '@' + domain).lower()
        digits = ''.join(filter(str.isdigit, s))
        local_number = '***-***-' + digits[-4:]
        if len(digits) == 10:
            return local_number
        country_code = '+' + '*' * (len(digits) - 10) + '-'
        return country_code + local_number