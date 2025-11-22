class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def is_valid_ipv4_block(block: str) -> bool:
            if block.isdigit():
                num = int(block)
                # Check range and no leading zeros except '0' itself
                return 0 <= num <= 255 and str(num) == block
            return False

        def is_valid_ipv6_block(block: str) -> bool:
            length = len(block)
            if 1 <= length <= 4:
                try:
                    int(block, 16)
                    return True
                except ValueError:
                    return False
            return False

        parts_ipv4 = queryIP.split('.')
        parts_ipv6 = queryIP.split(':')

        if len(parts_ipv4) == 4 and all(is_valid_ipv4_block(part) for part in parts_ipv4):
            return "IPv4"
        elif len(parts_ipv6) == 8 and all(is_valid_ipv6_block(part) for part in parts_ipv6):
            return "IPv6"
        else:
            return "Neither"