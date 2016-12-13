def hex_char_to_int(char):
    char = char.upper()
    if ord(char) <= ord('9'): return int(char)
    return 10 + ord(char) - ord('A')

def hex_string_to_int(string):
    intValue = 0;

    for i in range(len(string)):
        intValue = intValue * 16 + hex_char_to_int(string[i])

    return intValue
