import re

class Solution:
    def isValid(self, code: str) -> bool:
        # Remove all CDATA sections
        code = re.sub(r'<!\[CDATA\[.*?\]\]>', '', code)

        stack = []
        i = 0
        n = len(code)

        while i < n:
            if code[i] == '<':
                j = code.find('>', i + 1)
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
                    # Any tag starting with '!' (except CDATA which are removed) is invalid
                    return False
                else:
                    if not (1 <= len(tag_content) <= 9 and tag_content.isupper()):
                        return False
                    stack.append(tag_content)

                i = j + 1
            else:
                i += 1

        # Ensure stack is empty and there is at least one pair of properly formed tags
        if stack:
            return False

        # Check at least one opening and closing uppercase tag pair exists
        # Using regex to confirm at least one tag in the original code
        # Opens and closes tags with uppercase letters only
        # Pattern: <TAGNAME> ... </TAGNAME>
        tags_match = re.search(r'<([A-Z]{1,9})>.*?</\1>', code, re.DOTALL)
        return tags_match is not None