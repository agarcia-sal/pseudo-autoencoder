import re

class Solution:
    def isValid(self, code: str) -> bool:
        # Remove all CDATA sections
        cdata_pattern = re.compile(r'<!\[CDATA\[.*?\]\]>')
        code = cdata_pattern.sub('', code)

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

                if tag_content.startswith('/'):
                    tag_name = tag_content[1:]
                    if not stack or stack[-1] != tag_name:
                        return False
                    stack.pop()
                elif tag_content.startswith('!'):
                    # Tags starting with "!" not inside CDATA are invalid per logic
                    return False
                else:
                    # Tag name length check and uppercase check
                    if len(tag_content) < 1 or len(tag_content) > 9 or tag_content.upper() != tag_content:
                        return False
                    stack.append(tag_content)
                i = j + 1
            else:
                i += 1

        # pattern_check as per pseudocode: find all occurrences matching the pattern
        # <[A-Z]+>.*?</[A-Z]+>
        pattern_check = re.findall(r'<[A-Z]+>.*?</[A-Z]+>', code)

        return not stack and len(pattern_check) > 0