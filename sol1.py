braille = {
    'a': "100000",
    'b': "110000",
    'c': "100100",
    'd': "100110",
    'e': "100010",
    'f': "110100",
    'g': "110110",
    'h': "110010",
    'i': "010100",
    'j': "010110",
    'k': "101000",
    'l': "111000",
    'm': "101100",
    'n': "101110",
    'o': "101010",
    'p': "111100",
    'q': "111110",
    'r': "111010",
    's': "011100",
    't': "011110",
    'u': "101001",
    'v': "111001",
    'w': "010111",
    'x': "101101",
    'y': "101111",
    'z': "101011",
    ' ': "000000",
    'ccap': "000001",
    'wcap': "000001000001"
}

def solution(s):
    o = ""
    S = s.split(" ")
    i = 0   # index of the word in the sentence
    l = len(S)
    for w in S:
        i+=1
        wcap = False
        if w.isupper():
            o+=braille["wcap"]
            wcap = True
        for c in w:
            if not wcap and c.isupper():
                o+=braille["ccap"]
            o+=braille[c.lower()]
        if(i!=l):   #unless it is the last word, add a space
            o+=braille[" "]
    return o

print(solution("Braille"))