# Basic string compression and decompression.
def compress_string(s):
    if not s:
        return ""

    compressed_str = ""
    count = 1
    prev_char = s[0]

    for char in s[1:]:
        if char == prev_char:
            count += 1
        else:
            compressed_str += prev_char + str(count)
            prev_char = char
            count = 1

    compressed_str += prev_char + str(count)
    return compressed_str

def decompress_string(s):
    if not s:
        return ""

    decompressed_str = ""
    i = 0
    while i < len(s):
        char = s[i]
        i += 1
        count = ""
        while i < len(s) and s[i].isdigit():
            count += s[i]
            i += 1
        decompressed_str += char * int(count)
    return decompressed_str

original_string = "aaabbcca"
compressed_string = compress_string(original_string)
decompressed_string = decompress_string(compressed_string)

print(f"Original: {original_string}")
print(f"Compressed: {compressed_string}")
print(f"Decompressed: {decompressed_string}")