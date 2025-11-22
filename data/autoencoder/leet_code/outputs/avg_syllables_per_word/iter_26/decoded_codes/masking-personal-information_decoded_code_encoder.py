class Solution:
    def maskPII(self, string_input: str) -> str:
        if '@' in string_input:
            local_part, domain_part = string_input.split('@')
            masked_local_part = local_part[0] + '*' * 5 + local_part[-1]
            return masked_local_part.lower() + '@' + domain_part.lower()
        else:
            digit_characters = ''.join(filter(str.isdigit, string_input))
            local_phone_number = '***-***-' + digit_characters[-4:]
            if len(digit_characters) == 10:
                return local_phone_number
            else:
                country_code_length = len(digit_characters) - 10
                country_code_mask = '+' + '*' * country_code_length + '-'
                return country_code_mask + local_phone_number