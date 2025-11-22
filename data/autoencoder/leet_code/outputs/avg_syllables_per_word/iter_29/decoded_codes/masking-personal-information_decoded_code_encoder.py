class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            split_position = s.index('@')
            local_part = s[:split_position]
            domain_part = s[split_position + 1:]
            masked_local = local_part[0].lower() + '*****' + local_part[-1].lower()
            result_email = masked_local + '@' + domain_part.lower()
            return result_email
        else:
            all_characters = ''.join(ch for ch in s if ch.isdigit())
            digits_length = len(all_characters)
            local_number = '***-***-' + all_characters[-4:]
            if digits_length == 10:
                return local_number
            else:
                country_code_length = digits_length - 10
                country_code = '+' + ('*' * country_code_length) + '-'
                result_phone = country_code + local_number
                return result_phone