from collections import defaultdict

class Solution:
    def subdomainVisits(self, cpdomains):
        domain_count = self.get_default_dict_with_int_default()
        for cpdomain in cpdomains:
            count_and_domain = self.split_string_by_whitespace(cpdomain)
            count_string = count_and_domain[0]
            domain = count_and_domain[1]
            count = self.convert_string_to_integer(count_string)
            subdomains = self.split_string_by_period(domain)

            for index in range(len(subdomains)):
                subdomain_list = subdomains[index:]
                subdomain = self.join_list_with_period(subdomain_list)
                domain_count[subdomain] += count

        result_list = self.create_list()
        for domain_key, count_value in domain_count.items():
            formatted_string = self.format_count_and_domain(count_value, domain_key)
            result_list.append(formatted_string)

        return result_list

    def get_default_dict_with_int_default(self):
        return defaultdict(int)

    def split_string_by_whitespace(self, input_string):
        return input_string.split()

    def convert_string_to_integer(self, input_string):
        return int(input_string)

    def split_string_by_period(self, input_string):
        return input_string.split('.')

    def join_list_with_period(self, list_of_strings):
        return '.'.join(list_of_strings)

    def create_list(self):
        return []

    def format_count_and_domain(self, count_value, domain_string):
        return f"{count_value} {domain_string}"