def bin2dec(bits: str) -> int:
    pass 

# i would redo this preferably as str -> str
def hex2Base64(num: int) -> str:
    BASE64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    binary_stream = bin(num)[2:]
    output = ""
    paddings = 0

    for i in range(0, len(binary_stream), 6):
        sextet = binary_stream[i:i+6]

        if len(sextet) < 6:
            sextet += "0" * (6 - len(sextet)%6)

            if (6 - len(sextet)%6) == 2:
                paddings += 1
            else:
                paddings += 2

        output += BASE64[int(sextet, 2)] # replace with a simple binary->decimal implementation

    return output + "="*paddings

# testing below
# testing below

print(hex2Base64(0x1)) # 3q2+7w==

# 110111 3
# 101010 q
# 110110 2
# 111110 +
# 111011 7
# 11     w
#   0000 ==

def test():
    test = [
        0x1, 0xDEADBEEF, 0xABCDEF, 0x123456789, 0x1998BEE0DE55
    ]
    output = [
        "AQ==", "3q2+7w==", "q83v", "EjRWeAk=", "GZi+4N5V"
    ]
    for i in range(len(test)):
        print('\033[92m' + "PASS" + '\033[0m', end=" ") if hex2Base64(test[i]) == output[i] else print('\033[93m' + "FAIL" + '\033[0m', end=" ")
        print(hex2Base64(test[i]))

# test()