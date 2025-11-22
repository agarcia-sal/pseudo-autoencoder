def validIPAddress(IP):
    is_ipv4_block = lambda b: b.isdigit() and 0 <= int(b) <= 255 and str(int(b)) == b
    is_ipv6_block = lambda b: 1 <= len(b) <= 4 and all(c in "0123456789abcdefABCDEF" for c in b)
    parts4, parts6 = IP.split('.'), IP.split(':')
    if len(parts4) == 4 and all(is_ipv4_block(p) for p in parts4):
        return "IPv4"
    if len(parts6) == 8 and all(is_ipv6_block(p) for p in parts6):
        return "IPv6"
    return "Neither"