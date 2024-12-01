l = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]


def solution(l):
    out = []
    for i in range(len(l)):
        l[i] = l[i].split(".")
        while len(l[i]) < 3:
            l[i].append("-1")
        for j in range(len(l[i])):
            l[i][j] = int(l[i][j])

    l = sorted(l, key=lambda id: id[0])
    print("l", l)
    Mv = []
    for i in l:
        if i[0] not in Mv:
            Mv.append(i[0])
    for i in Mv:
        minor = []
        for j in l:
            if j[0] == i:
                minor.append(j)
        minor = sorted(minor, key=lambda id: id[1])
        print("minor", minor)
        mv = []
        for j in minor:
            if j[1] not in mv:
                mv.append(j[1])
        for j in mv:
            rev = []
            for k in minor:
                if k[1] == j:
                    rev.append(k)
            rev = sorted(rev, key=lambda id: id[2])
            print("rev", rev)
            for k in range(len(rev)):
                out.append(".".join([str(l) for l in rev[k] if l != -1]))
    return out


print(solution(l))
