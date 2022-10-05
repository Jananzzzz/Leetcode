def match(a, b):
    if not a: return not b         # while a != b, return true; a == b == 0, return true
    first_match = bool(b) and a[0] in {b[0], '.'}
    return first_match and match(a[1:], b[1:])

    
    # '*' Matches zero or more of the preceding element.