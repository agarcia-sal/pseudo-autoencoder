import re

class Solution:
    def isValid(self, code: str) -> bool:
        # Pattern for CDATA sections: <![CDATA[...]]>
        cdata_pattern = re.compile(r'<!\[CDATA\[.*?\]\]>')
        # Remove all CDATA sections
        code = cdata_pattern.sub('', code)

        stack = []
        i = 0
        n = len(code)
        while i < n:
            if code[i] == '<':
                j = code.find('>', i + 1)
                if j == -1:
                    return False  # No matching '>'
                tag_content = code[i+1:j]
                if not tag_content:
                    return False  # Empty tag
                if tag_content[0] == '/':
                    tag_name = tag_content[1:]
                    if not stack or stack[-1] != tag_name:
                        return False  # Mismatched or unbalanced tag
                    stack.pop()
                elif tag_content[0] == '!':
                    # CDATA should have been removed already; invalid if found here
                    return False
                else:
                    if not (1 <= len(tag_content) <= 9 and tag_content.isupper()):
                        return False  # Invalid tag name
                    stack.append(tag_content)
                i = j + 1
            else:
                i += 1

        # Ensure stack is empty and code contains at least one valid top-level tag
        pattern = re.compile(r'<[A-Z]+>.*</[A-Z]+>', re.DOTALL)
        return not stack and bool(pattern.search(code))