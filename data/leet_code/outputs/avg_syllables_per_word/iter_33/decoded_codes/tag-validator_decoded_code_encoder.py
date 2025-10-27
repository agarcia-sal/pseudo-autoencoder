import re

class Solution:
    def isValid(self, code: str) -> bool:
        cdata_pattern = re.compile(r'<!\[CDATA\[.*?\]\]>')
        code = cdata_pattern.sub('', code)
        stack = []
        i = 0
        length = len(code)
        while i < length:
            if code[i] == '<':
                j = code.find('>', i + 1)
                if j == -1:
                    return False
                tag_content = code[i + 1:j]
                if len(tag_content) == 0:
                    return False
                if tag_content[0] == '/':
                    tag_name = tag_content[1:]
                    if not stack or stack[-1] != tag_name:
                        return False
                    stack.pop()
                elif tag_content[0] == '!':
                    return False
                else:
                    if len(tag_content) < 1 or len(tag_content) > 9 or not tag_content.isupper():
                        return False
                    stack.append(tag_content)
                i = j + 1
            else:
                i += 1
        valid_tag_pattern = re.compile(r'<[A-Z]+>.*</[A-Z]+>', re.DOTALL)
        return not stack and bool(valid_tag_pattern.search(code))