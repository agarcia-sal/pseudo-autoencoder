from collections import defaultdict
from typing import List

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_count = defaultdict(int)
        for cpdomain in cpdomains:
            count_str, domain = cpdomain.split()
            count = int(count_str)
            subdomains = domain.split('.')
            for index in range(len(subdomains)):
                subdomain = '.'.join(subdomains[index:])
                domain_count[subdomain] += count
        result = [f"{cnt} {dom}" for dom, cnt in domain_count.items()]
        return result