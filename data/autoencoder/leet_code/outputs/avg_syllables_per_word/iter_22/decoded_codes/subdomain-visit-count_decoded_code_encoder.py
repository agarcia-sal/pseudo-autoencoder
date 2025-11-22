from collections import defaultdict

class Solution:
    def subdomainVisits(self, cpdomains):
        domain_count = defaultdict(int)
        for cpdomain in cpdomains:
            count_text, domain_text = cpdomain.split(' ', 1)
            count = int(count_text)
            subdomains = domain_text.split('.')
            for i in range(len(subdomains)):
                subdomain = '.'.join(subdomains[i:])
                domain_count[subdomain] += count
        result = []
        for domain_key, count_value in domain_count.items():
            formatted_string = f"{count_value} {domain_key}"
            result.append(formatted_string)
        return result