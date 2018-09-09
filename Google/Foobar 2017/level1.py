__author__ = 'liuweizhi'

# the initial data
data = {"code": "100100101010100110100010",
        "Braille": "000001110000111010100000010100111000111000100010",
        "The quick brown fox jumped over the lazy dog": "000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100100010100110000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110"}

# construct the code book
code = {'s':"011100"} # see https://en.wikipedia.org/wiki/Braille
for k, v in data.iteritems():
    i = 0
    for character in k:
        if character.isspace():
            code[character] = v[i:i+6]
        if character.isupper():
            code["UPPER"] = v[i:i+6]
            i += 6
            code[character.lower()] = v[i:i+6]
        if character.islower():
            code[character] = v[i:i+6]
        i += 6

# the parse function
def answer(plaintext):
    # your code here
    ans = ""
    for character in plaintext:
        if character.isupper():
            ans += code["UPPER"]
        ans += code[character.lower()]
    return ans
