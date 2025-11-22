import re
from typing import List

class Solution:
    def isValid(self, code: str) -> bool:
        cdata_pattern = r'<!\[CDATA\[.*?\]\]>'
        code = re.sub(cdata_pattern, '', code)

        stack: List[str] = []
        i = 0
        n = len(code)

        while i < n:
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
                    # According to the pseudocode, any tag_content starting with '!' returns False
                    return False
                else:
                    # tag name must be length 1..9 and all uppercase letters
                    if not (1 <= len(tag_content) <= 9 and tag_content.isupper()):
                        return False
                    stack.append(tag_content)

                i = j + 1
            else:
                i += 1

        # validate presence of at least one valid closed tag pair with uppercase letters
        valid_tag_presence = re.findall(r'<[A-Z]{1,9}>.*?</[A-Z]{1,9}>', code, re.DOTALL)

        return len(stack) == 0 and len(valid_tag_presence) > 0