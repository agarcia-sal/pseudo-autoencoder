import re

class Solution:
    def isValid(self, code: str) -> bool:
        # Pattern to detect CDATA sections
        cdata_pattern = re.compile(r'<!\[CDATA\[.*?\]\]>', re.DOTALL)
        # Remove all CDATA sections from code
        code = cdata_pattern.sub('', code)

        stack = []
        i = 0
        n = len(code)

        while i < n:
            if code[i] == '<':
                j = code.find('>', i + 1)
                if j == -1:
                    return False  # No closing '>' found for tag

                tag_content = code[i + 1:j]
                if not tag_content:
                    return False  # Empty tag

                if tag_content[0] == '/':
                    tag_name = tag_content[1:]
                    if not stack or stack[-1] != tag_name:
                        return False  # Mismatched or unbalanced closing tag
                    stack.pop()
                elif tag_content[0] == '!':
                    return False  # CDATA section found after removal
                else:
                    # Opening tag name validity check
                    if not (1 <= len(tag_content) <= 9) or not tag_content.isupper():
                        return False  # Invalid tag name
                    stack.append(tag_content)

                i = j + 1
            else:
                i += 1

        # Final checks: stack must be empty and at least one valid tag pair must exist
        tag_pair_pattern = re.compile(r'<[A-Z]+>.*?</[A-Z]+>', re.DOTALL)
        return not stack and bool(tag_pair_pattern.search(code))