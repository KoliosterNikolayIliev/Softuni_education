def solution(s):
    if len(s) % 2 != 0:
        s += "_"
    l = []
    for i in range(len(s)):
        if i % 2 == 0:
            l.append(s[i]+s[i+1])
    return l


str1 = ""
print(solution(str1))
