import re

class Solution:
    def isValid(self, code: str) -> bool:
        # Pattern for CDATA sections
        cdata_pattern = re.compile(r"<!\[CDATA\[.*?\]\]>")
        # Remove all CDATA sections from code
        code = cdata_pattern.sub("", code)

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
                    # Any tag starting with '!' other than CDATA is invalid
                    return False
                else:
                    # Tag name must be 1 to 9 uppercase letters
                    if not (1 <= len(tag_content) <= 9) or not all('A' <= ch <= 'Z' for ch in tag_content):
                        return False
                    stack.append(tag_content)
                i = j + 1
            else:
                i += 1

        valid_tag_pattern = re.compile(r"<[A-Z]+>.*</[A-Z]+>", re.DOTALL)
        return not stack and valid_tag_pattern.search(code) is not None