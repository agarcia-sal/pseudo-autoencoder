class Solution:
    def validIPAddress(self, queryIP):
        def is_valid_ipv4_block(block):
            if block.isdigit():
                num = int(block)
                # Check 0 <= num <= 255 and no leading zeros (except for '0')
                return 0 <= num <= 255 and str(num) == block
            return False

        def is_valid_ipv6_block(block):
            if 1 <= len(block) <= 4:
                try:
                    int(block, 16)
                    return True
                except ValueError:
                    return False
            return False

        parts_ipv4 = queryIP.split('.')
        parts_ipv6 = queryIP.split(':')

        if len(parts_ipv4) == 4 and all(is_valid_ipv4_block(b) for b in parts_ipv4):
            return "IPv4"
        elif len(parts_ipv6) == 8 and all(is_valid_ipv6_block(b) for b in parts_ipv6):
            return "IPv6"
        else:
            return "Neither"