class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            local, domain = self.split_string(s, '@')
            masked_local = self.mask_local_part(local)
            lowercase_masked_local = self.convert_to_lowercase(masked_local)
            lowercase_domain = self.convert_to_lowercase(domain)
            result = lowercase_masked_local + '@' + lowercase_domain
            return result
        else:
            digits = self.extract_digits(s)
            local_number = self.construct_local_phone_number(digits)
            if len(digits) == 10:
                return local_number
            else:
                country_code_length = self.determine_country_code_length(digits, 10)
                country_code = self.construct_country_code_mask(country_code_length)
                result = country_code + local_number
                return result

    def split_string(self, string_value: str, separator: str) -> tuple[str, str]:
        part_before, part_after = string_value.split(separator, 1)
        return part_before, part_after

    def mask_local_part(self, local_part: str) -> str:
        # First character + 5 asterisks + last character
        return local_part[0] + '*****' + local_part[-1]

    def convert_to_lowercase(self, input_string: str) -> str:
        return input_string.lower()

    def extract_digits(self, input_string: str) -> str:
        return ''.join(c for c in input_string if c.isdigit())

    def construct_local_phone_number(self, digits_string: str) -> str:
        # Format as ***-***-last4_digits
        return '***-***-' + digits_string[-4:]

    def determine_country_code_length(self, digits_string: str, base_length: int) -> int:
        return len(digits_string) - base_length

    def construct_country_code_mask(self, length: int) -> str:
        return '+' + ('*' * length) + '-'