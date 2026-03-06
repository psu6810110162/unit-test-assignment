def caesar_cipher(s: str, k: int) -> str:
    
    result = []
    for char in s:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + k) % 26 + base
            result.append(chr(shifted))
        else:
            result.append(char)
    return "".join(result)