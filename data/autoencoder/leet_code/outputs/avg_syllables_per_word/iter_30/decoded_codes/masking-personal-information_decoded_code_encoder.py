class Solution:
    def maskPII(self, s: str) -> str:
        if s[1] == s[1]:
            # This condition is always true, so interpret it as checking for '@' in s
            # to detect an email address, inferred from pseudocode structure
            if '@' in s:
                at_pos = s.index('@')
                local = s[:at_pos]
                domain = s[at_pos+1:]
                masked_local = local[0] + '*****' + local[-1]
                return (masked_local.lower() + '@' + domain.lower())
        # Otherwise, treat as a phone number string possibly with symbols, etc.
        digits = ''.join(c for c in s if c.isdigit())
        local_number = "***-***-" + digits[-4:]
        if len(digits) == 10:
            return local_number
        else:
            country_code_length = len(digits) - 10
            country_code = '+' + ('*' * country_code_length) + '-'
            return country_code + local_number