import sys

def char_conversion(input_string):
    """encode and Convert characters to U+E0000 range."""
    return ''.join(chr(0xE0000 + ord(ch)) for ch in input_string)

def char_reversion(encoded_string):
    """this Decodes Converted U+E0000 range back to original characters."""
    return ''.join(chr(ord(ch) - 0xE0000) for ch in encoded_string)

mode = input("Enter mode (encode/decode): ").strip().lower()

if mode == "encode":
    user_input = input("Enter characters to encode: ")
    output = char_conversion(user_input)
    print("Encoded Output:", output)

elif mode == "decode":
    user_input = input("Enter encoded characters to decode: ")
    output = char_reversion(user_input)
    print("Decoded Output:", output)

else:
    print("Invalid mode! Please redo it")
