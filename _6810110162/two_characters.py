from itertools import combinations


def two_characters(s: str) -> int:
    
    if len(s) < 2:
        return 0

    unique_chars = set(s)
    if len(unique_chars) < 2:
        return 0

    best = 0
    for a, b in combinations(unique_chars, 2):
        filtered = [c for c in s if c in (a, b)]
        valid = True
        for i in range(1, len(filtered)):
            if filtered[i] == filtered[i - 1]:
                valid = False
                break
        if valid and len(filtered) > best:
            best = len(filtered)

    return best