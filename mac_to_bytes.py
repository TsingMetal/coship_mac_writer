"""
the build-in module binascii could be used:
binascii.a2b_hex(hexString)
or simply use:
bytes.fromhex(hexString)!
"""

from hex_string_to_int import hex_string_to_int


def mac_string_to_bytes(mac):
    '''
    1, divide a mac string into 4 groups,
    2, each group contains a 2-charactored hex string,
    3, convert each group to an integer,
    4, then convert each integer to a charactor,
    5, conbine all charactors to a string,
    6, encode the string to bytes by encoding latin1
    '''
    assert len(mac) == 12
    lst = []
    for i in range(0, 12, 2):
        lst.append(mac[i : i+2])

    string = ''
    for i in lst:
        j = hex_string_to_int(i)
        k = chr(j)
        string += k

    return string.encode("latin1")

    # alternative:
    s = ''
    for i in range(0, 12, 2):
        s += chr(hex_string_to_int(mac[i : i+2]))

    return s


if __name__ == '__main__':
    import sys
    mac = '68db67447f0d'
    if len(sys.argv) > 1:
        mac = sys.argv[1]
    header = b'\xf1\xf2\xf3\xf4'
    open("mac.bin", 'wb').write(header + mac_string_to_bytes(mac))
