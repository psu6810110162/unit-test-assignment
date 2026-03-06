def funny_string(s: str) -> str:
   
    forward = [abs(ord(s[i]) - ord(s[i - 1])) for i in range(1, len(s))]
    backward = [abs(ord(s[i]) - ord(s[i + 1])) for i in range(len(s) - 2, -1, -1)]
    return "Funny" if forward == backward else "Not Funny"