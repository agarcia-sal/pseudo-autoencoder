import re

class Solution:
    def isValid(self, code: str) -> bool:
        # Pattern for CDATA sections: <![CDATA[...]]>
        cdata_pattern = r'<!\[CDATA\[.*?\]\]>'

        # Remove all CDATA sections from code
        code = re.sub(cdata_pattern, '', code)

        stack = []
        i = 0
        n = len(code)

        while i < n:
            if code[i] == '<':
                j = code.find('>', i + 1)
                if j == -1:
                    return False  # No matching '>'

                tag_content = code[i + 1:j]
                if not tag_content:
                    return False  # Empty tag content

                first_char = tag_content[0]

                if first_char == '/':
                    tag_name = tag_content[1:]
                    if not stack or stack[-1] != tag_name:
                        return False  # Closing tag does not match last opened tag
                    stack.pop()
                elif first_char == '!':
                    # CDATA sections should have been removed
                    return False
                else:
                    tag_name = tag_content
                    # Tag name must be 1 to 9 chars and all uppercase A-Z
                    if not (1 <= len(tag_name) <= 9 and tag_name.isupper()):
                        return False
                    stack.append(tag_name)
                i = j + 1
            else:
                i += 1

        # At end, stack must be empty and at least one valid opening-closing tag pair exist
        # Pattern: <[A-Z]+>.*</[A-Z]+>
        valid_tag_pair_pattern = r'<[A-Z]+>.*?</[A-Z]+>'
        return not stack and re.search(valid_tag_pair_pattern, code) is not None