import re

class Solution:
    def isValid(self, code: str) -> bool:
        cdata_pattern = r"<!\[CDATA\[.*?\]\]>"
        code = re.sub(cdata_pattern, "", code)
        stack = []
        i = 0
        length = len(code)

        while i < length:
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
                    if not (1 <= len(tag_content) <= 9) or tag_content.upper() != tag_content:
                        return False
                    stack.append(tag_content)
                i = j + 1
            else:
                i += 1

        is_balanced = not stack
        has_valid_tag = bool(
            re.search(
                r"<[A-Z]+>.*?</[A-Z]+>",
                code
            )
        )
        return is_balanced and has_valid_tag