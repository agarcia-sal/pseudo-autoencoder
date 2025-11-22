from collections import defaultdict
from typing import List

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_count = defaultdict(int)
        for cpdomain in cpdomains:
            count_and_domain = cpdomain.split(' ')
            count = int(count_and_domain[0])
            domain = count_and_domain[1]
            subdomains = domain.split('.')
            for index in range(len(subdomains)):
                subdomain_elements = subdomains[index:]
                subdomain = '.'.join(subdomain_elements)
                domain_count[subdomain] += count
        result = [f"{count} {domain}" for domain, count in domain_count.items()]
        return result