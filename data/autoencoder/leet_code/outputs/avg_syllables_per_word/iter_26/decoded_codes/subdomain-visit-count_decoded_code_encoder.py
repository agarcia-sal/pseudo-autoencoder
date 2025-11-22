from collections import defaultdict

class Solution:
    def subdomainVisits(self, cpdomains):
        domain_count = defaultdict(int)

        for cpdomain in cpdomains:
            count_string, domain = cpdomain.split(" ")
            count = int(count_string)
            subdomains = domain.split(".")

            for i in range(len(subdomains)):
                subdomain = ".".join(subdomains[i:])
                domain_count[subdomain] += count

        result_list = [f"{count} {domain}" for domain, count in domain_count.items()]
        return result_list