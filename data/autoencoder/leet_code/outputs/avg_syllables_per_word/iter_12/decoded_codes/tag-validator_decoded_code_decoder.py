import re

class Solution:
    def isValid(self, code: str) -> bool:
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
                tag_content = code[i + 1:j]
                if not tag_content:
                    return False
                if tag_content[0] == '/':
                    tag_name = tag_content[1:]
                    if not stack or stack[-1] != tag_name:
                        return False
                    stack.pop()
                elif tag_content[0] == '!':
                    # Tags starting with '!' other than CDATA (already removed) are invalid
                    return False
                else:
                    if not (1 <= len(tag_content) <= 9 and tag_content.isupper()):
                        return False
                    stack.append(tag_content)
                i = j + 1
            else:
                i += 1
        # The code is valid if stack is empty and there was at least one valid tag pair
        return not stack and bool(re.findall(r'<[A-Z]+>.*?</[A-Z]+>', code))