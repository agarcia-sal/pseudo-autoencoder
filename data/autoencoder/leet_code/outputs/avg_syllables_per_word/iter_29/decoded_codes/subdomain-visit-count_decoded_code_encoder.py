from collections import defaultdict

class Solution:
    def subdomainVisits(self, cpdomains):
        domain_count = defaultdict(int)

        for cpdomain in cpdomains:
            count_string, domain_string = cpdomain.split()
            count = int(count_string)
            subdomains = domain_string.split('.')

            for i in range(len(subdomains)):
                subdomain = '.'.join(subdomains[i:])
                domain_count[subdomain] += count

        result_list = []
        for domain, count in domain_count.items():
            result_list.append(f"{count} {domain}")

        return result_list