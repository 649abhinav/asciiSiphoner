Usage:
1. Script create UTF-16 surrogate pair from input unicode tag chracters , which completely invisible to some of client side parsers to bypass it.
2. After input some value it creates utf-16 string eg: admin = \udb40\udc61\udb40\udc64\udb40\udc6d\udb40\udc69\udb40\udc6e
3. Which each individual tag character and re-encode it with an offset of 0xE0000
 print(''.join(chr(ord(c)-0xE0000) for c in '\udb40\udc61\udb40\udc64\udb40\udc6d\udb40\udc69\udb40\udc6e'.encode('utf-16', 'surrogatepass').decode('utf-16') if ord(c) >= 0xE0000))

--->admin<--- 
