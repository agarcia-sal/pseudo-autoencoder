def ip_to_int(ip):
    return sum(int(part) << (8 * (3 - i)) for i, part in enumerate(ip.split('.')))

def int_to_ip(num):
    return '.'.join(str((num >> (8 * i)) & 255) for i in reversed(range(4)))

def largest_cidr_size(start, n):
    if start & 1:
        return 1
    x = 1
    while x <= n and (start & (x - 1)) == 0:
        x <<= 1
    return x >> 1

def ip_to_cidrs(ip, n):
    start = ip_to_int(ip)
    res = []
    while n > 0:
        size = largest_cidr_size(start, n)
        prefix_len = 32 - (size.bit_length() - 1)
        res.append(f"{int_to_ip(start)}/{prefix_len}")
        start += size
        n -= size
    return res