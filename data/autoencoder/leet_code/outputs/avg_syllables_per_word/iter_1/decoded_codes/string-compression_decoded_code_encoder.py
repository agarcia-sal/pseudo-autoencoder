def compress(chars):
    if not chars:
        return 0
    wi, ri = 0, 0
    while ri < len(chars):
        c = chars[ri]
        count = 0
        while ri < len(chars) and chars[ri] == c:
            ri += 1
            count += 1
        chars[wi] = c
        wi += 1
        if count > 1:
            for d in str(count):
                chars[wi] = d
                wi += 1
    return wi