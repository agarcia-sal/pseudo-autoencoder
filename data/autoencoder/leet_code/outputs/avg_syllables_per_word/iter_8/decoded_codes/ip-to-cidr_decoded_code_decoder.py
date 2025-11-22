class Solution:
    def ipToCIDR(self, ip, n):
        def ip_to_int(ip):
            parts = list(map(int, ip.split('.')))
            res = 0
            for part in parts:
                res = (res << 8) + part
            return res

        def int_to_ip(num):
            list_of_segments = []
            for i in range(3, -1, -1):
                segment = (num >> (8 * i)) & 255
                list_of_segments.append(str(segment))
            return '.'.join(list_of_segments)

        def largest_cidr_size(start, n):
            if start & 1 == 1:
                return 1
            x = 1
            while x <= n and (start & (x - 1)) == 0:
                x <<= 1
            return x >> 1

        result = []
        start_ip = ip_to_int(ip)

        while n > 0:
            size = largest_cidr_size(start_ip, n)
            prefix_length = 32 - (size.bit_length() - 1)
            result.append(int_to_ip(start_ip) + '/' + str(prefix_length))
            start_ip += size
            n -= size

        return result