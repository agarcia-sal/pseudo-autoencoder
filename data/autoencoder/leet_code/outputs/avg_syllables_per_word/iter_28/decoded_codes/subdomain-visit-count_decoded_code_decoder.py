from collections import defaultdict
from typing import List

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_count = defaultdict(int)
        for cpdomain in cpdomains:
            count_string, domain_string = cpdomain.split(' ', 1)
            count = int(count_string)
            subdomains = domain_string.split('.')
            for i in range(len(subdomains)):
                subdomain = '.'.join(subdomains[i:])
                domain_count[subdomain] += count
        return [f"{v} {k}" for k, v in domain_count.items()]