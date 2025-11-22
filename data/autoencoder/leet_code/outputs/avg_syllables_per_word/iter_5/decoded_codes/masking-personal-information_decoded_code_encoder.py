class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            local, domain = s.split('@')
            masked_local = local[0] + "*****" + local[-1]
            return (masked_local + '@' + domain).lower()
        digits = [c for c in s if c.isdigit()]
        local_number = "***-***-" + "".join(digits[-4:])
        if len(digits) == 10:
            return local_number
        country_code = "+" + "*" * (len(digits) - 10) + "-"
        return country_code + local_number