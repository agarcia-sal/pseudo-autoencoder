import re

class Solution:
    def isValid(self, code: str) -> bool:
        # Pattern for CDATA sections: <![CDATA[...]]>
        cdata_pattern = r'<!\[CDATA\[.*?\]\]>'

        # Remove all CDATA sections
        code = re.sub(cdata_pattern, '', code)

        stack = []
        i = 0
        length = len(code)

        while i < length:
            if code[i] == '<':
                j = code.find('>', i + 1)
                if j == -1:
                    return False

                tag_content = code[i+1:j]
                if not tag_content:
                    return False

                if tag_content[0] == '/':
                    # Closing tag
                    tag_name = tag_content[1:]
                    if not stack or stack[-1] != tag_name:
                        return False
                    stack.pop()
                elif tag_content[0] == '!':
                    # Per specification, any tag starting with '!' is invalid here
                    return False
                else:
                    # Opening tag: tag_content must be 1 to 9 chars, all uppercase letters
                    if not (1 <= len(tag_content) <= 9) or not tag_content.isupper():
                        return False
                    stack.append(tag_content)

                i = j + 1
            else:
                i += 1

        # If stack is empty and there is at least one valid top-level tag, it is valid
        # Check if stack is empty and the code contains at least one valid uppercase tag properly nested
        # The pattern: <TAG>...</TAG>, where TAG is 1-9 uppercase letters
        pattern = r'<([A-Z]{1,9})>.*</\1>'
        return not stack and bool(re.search(pattern, code))