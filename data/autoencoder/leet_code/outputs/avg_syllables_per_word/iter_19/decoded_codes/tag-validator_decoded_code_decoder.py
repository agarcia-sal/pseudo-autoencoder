import re

class Solution:
    def isValid(self, code):
        # Remove all CDATA content
        cdata_pattern = r'<!\[CDATA\[.*?\]\]>'
        code = re.sub(cdata_pattern, '', code)

        stack = []
        i = 0
        n = len(code)

        while i < n:
            if code[i] == '<':
                j = code.find('>', i + 1)
                if j == -1:
                    return False

                tag_content = code[i+1:j]
                if not tag_content:
                    return False

                if tag_content[0] == '/':
                    tag_name = tag_content[1:]
                    if not stack or stack[-1] != tag_name:
                        return False
                    stack.pop()
                elif tag_content[0] == '!':
                    # Any tag starting with '!' after removing CDATA is invalid
                    return False
                else:
                    if not (1 <= len(tag_content) <= 9) or not tag_content.isupper():
                        return False
                    stack.append(tag_content)
                i = j + 1
            else:
                i += 1

        # Check stack is empty (all tags closed) and code contains at least one valid top-level tag pair
        pattern = r'<[A-Z]+>.*?</[A-Z]+>'
        return not stack and re.search(pattern, code) is not None