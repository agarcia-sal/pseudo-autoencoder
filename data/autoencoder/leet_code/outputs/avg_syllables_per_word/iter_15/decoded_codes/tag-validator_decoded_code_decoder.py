import re

class Solution:
    def isValid(self, code: str) -> bool:
        cdata_pattern = re.compile(r'<![A-Z]*?\[.*?\]>')
        code = cdata_pattern.sub('', code)
        stack = []
        i = 0
        n = len(code)
        while i < n:
            if code[i] == '<':
                j = code.find('>', i)
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
                    return False
                else:
                    if len(tag_content) < 1 or len(tag_content) > 9 or not tag_content.isupper():
                        return False
                    stack.append(tag_content)
                i = j + 1
            else:
                i += 1
        if stack:
            return False
        # pattern to check tag pairs <TAG>...</TAG> where TAG is uppercase letters
        pattern = re.compile(r'<([A-Z]{1,9})>.*?</\1>', re.DOTALL)
        return bool(pattern.search(code))