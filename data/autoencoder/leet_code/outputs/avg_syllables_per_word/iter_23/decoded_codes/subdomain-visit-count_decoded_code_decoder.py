from collections import defaultdict
from typing import List

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_count = defaultdict(int)
        for cpdomain in cpdomains:
            count_string, domain_string = cpdomain.split(maxsplit=1)
            count = int(count_string)
            subdomains = domain_string.split('.')
            for index in range(len(subdomains)):
                subdomain = '.'.join(subdomains[index:])
                domain_count[subdomain] += count
        result_list = []
        for domain, count in domain_count.items():
            result_list.append(f"{count} {domain}")
        return result_list