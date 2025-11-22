import re

class Solution:
    def isValid(self, code: str) -> bool:
        # Pattern for CDATA sections: <![CDATA[...]]>
        cdata_pattern = re.compile(r'<!\[CDATA\[.*?\]\]>')

        # Remove all CDATA sections from code
        code = cdata_pattern.sub('', code)

        stack = []
        i = 0
        n = len(code)

        while i < n:
            if code[i] == '<':
                j = code.find('>', i + 1)
                if j == -1:
                    return False  # no closing '>' found

                tag_content = code[i+1:j]
                if not tag_content:
                    return False  # empty tag content

                if tag_content[0] == '/':
                    tag_name = tag_content[1:]
                    if not stack or stack[-1] != tag_name:
                        return False  # mismatched or unbalanced tag
                    stack.pop()
                elif tag_content[0] == '!':
                    # Invalid presence of CDATA section here (should be removed before)
                    return False
                else:
                    if not (1 <= len(tag_content) <= 9) or tag_content != tag_content.upper():
                        return False  # invalid tag name
                    stack.append(tag_content)
                i = j + 1
            else:
                i += 1

        # Check that all tags are closed and there is at least one valid tag section
        # Regex to find valid tag sections of format <TAG>...</TAG> with uppercase tag names
        valid_tag_pattern = re.compile(r'<[A-Z]+>.*?</[A-Z]+>', re.DOTALL)
        valid_tags = valid_tag_pattern.findall(code)

        return len(stack) == 0 and len(valid_tags) > 0