from collections import defaultdict

class Solution:
    def subdomainVisits(self, cpdomains):
        domain_count = defaultdict(int)

        for cpdomain in cpdomains:
            count_and_domain = cpdomain.split()
            count = int(count_and_domain[0])
            domain = count_and_domain[1]
            subdomains = domain.split('.')

            for index in range(len(subdomains)):
                subdomain_parts = subdomains[index:]
                subdomain = '.'.join(subdomain_parts)
                domain_count[subdomain] += count

        result_list = [f"{count} {domain}" for domain, count in domain_count.items()]
        return result_list