import re

class Solution:
    def isValid(self, code: str) -> bool:
        # Remove all CDATA sections
        cdata_pattern = re.compile(r"<!\[CDATA\[.*?\]\]>")
        code = cdata_pattern.sub("", code)

        stack = []
        i = 0
        n = len(code)

        while i < n:
            if code[i] == '<':
                j = code.find('>', i + 1)
                if j == -1:
                    return False
                tag_content = code[i + 1 : j]
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
                    if len(tag_content) < 1 or len(tag_content) > 9 or tag_content != tag_content.upper():
                        return False
                    stack.append(tag_content)
                i = j + 1
            else:
                i += 1

        # stack should be empty and there must be at least one valid tag structure in original code
        if stack:
            return False

        valid_tag_pattern = re.compile(r"<[A-Z]+>.*</[A-Z]+>")
        return bool(valid_tag_pattern.findall(code))