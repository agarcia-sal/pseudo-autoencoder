def mask_email_or_phone(s):
    if '@' in s:
        local, domain = s.split('@')
        return (local[0] + "*****" + local[-1]).lower() + "@" + domain.lower()
    else:
        digits = "".join(filter(str.isdigit, s))
        local_num = "***-***-" + digits[-4:]
        if len(digits) == 10:
            return local_num
        else:
            cc = "+" + "*" * (len(digits) - 10) + "-"
            return cc + local_num