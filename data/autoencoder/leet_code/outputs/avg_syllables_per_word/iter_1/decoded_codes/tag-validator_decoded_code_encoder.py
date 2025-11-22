import re

def isValid(code):
    # Remove all CDATA sections
    code = re.sub(r'<!\[CDATA\[.*?\]\]>', '', code, flags=re.DOTALL)

    stack = []
    i = 0
    n = len(code)

    while i < n:
        if code[i] == '<':
            j = code.find('>', i)
            if j == -1:
                return False

            tag = code[i+1:j]
            if not tag:
                return False

            if tag[0] == '/':  # closing tag
                if not stack or stack[-1] != tag[1:]:
                    return False
                stack.pop()
            elif tag[0] == '!':  # tags starting with !
                return False
            else:  # opening tag
                if not (1 <= len(tag) <= 9) or not tag.isupper():
                    return False
                stack.append(tag)
            i = j + 1
        else:
            i += 1

    # stack must be empty (all tags closed), 
    # and code must contain at least one valid <TAG> ... </TAG> with uppercase TAG,
    # i.e. must contain a tag at all (stack len was nonzero before closing fully)
    # We can check if there exists at least one <...> tag with uppercase inside

    # Quick test: search for any opening tag with 1-9 uppercase letters
    return not stack and bool(re.search(r'<[A-Z]{1,9}>', code))