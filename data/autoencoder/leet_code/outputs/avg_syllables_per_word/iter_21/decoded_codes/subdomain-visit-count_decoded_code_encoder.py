from collections import defaultdict

class Solution:
    def subdomainVisits(self, cpdomains):
        domain_count = defaultdict(int)

        for cpdomain in cpdomains:
            count_str, domain = cpdomain.split(' ')
            count = int(count_str)
            subdomains = domain.split('.')

            for i in range(len(subdomains)):
                subdomain = '.'.join(subdomains[i:])
                domain_count[subdomain] += count

        result_list = [f"{cnt} {dom}" for dom, cnt in domain_count.items()]

        return result_list