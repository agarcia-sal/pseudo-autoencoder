from collections import defaultdict

class Solution:
    def subdomainVisits(self, cpdomains):
        domain_count = defaultdict(int)

        for cpdomain in cpdomains:
            count_str, domain = cpdomain.split()
            count = int(count_str)
            subdomains = domain.split('.')

            for index in range(len(subdomains)):
                subdomain = '.'.join(subdomains[index:])
                domain_count[subdomain] += count

        result = []
        for domain, count in domain_count.items():
            result.append(f"{count} {domain}")

        return result