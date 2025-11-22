from collections import defaultdict

class Solution:
    def subdomainVisits(self, cpdomains):
        domain_count = defaultdict(int)

        for cpdomain in cpdomains:
            count_part, domain_part = cpdomain.split(' ', 1)
            count = int(count_part)
            subdomains = domain_part.split('.')

            for i in range(len(subdomains)):
                subdomain = '.'.join(subdomains[i:])
                domain_count[subdomain] += count

        result = [f"{count} {domain}" for domain, count in domain_count.items()]
        return result