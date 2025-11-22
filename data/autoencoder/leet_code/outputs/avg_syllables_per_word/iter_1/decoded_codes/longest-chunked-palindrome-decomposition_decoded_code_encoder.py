def process_text(text):
    L, R = 0, len(text) - 1
    LP, RP = "", ""
    k = 0
    while L < R:
        LP += text[L]
        RP = text[R] + RP
        if LP == RP:
            k += 2
            LP = RP = ""
        L += 1
        R -= 1
    if LP != "" or L == R:
        k += 1
    return k