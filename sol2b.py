def solution(s):
    count = 0
    for c in range(0, len(s)):
        if s[c] == ">":
            count += s[c:].count("<")
    return count * 2
