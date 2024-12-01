def count(x, y, c):
    m = int(x)
    f = int(y)
    if m == 1 and f == 1:  # it is possible to reach the given numbers from (1,1)
        return str(c)
    elif m < 1 or f < 1 or m == f:  # cases when it is impossible
        return "impossible"
    else:
        if m > f:
            if (
                m > 10 * f
            ):  # if the difference is large, we reduce the gap in one step to save execution time
                multi = int(m / f) - 1
                c += multi
                m -= multi * f
            else:
                m -= f  # for small differences, we just sumbtract the smaller from the larger
                c += 1
        else:
            if f > 10 * m:
                multi = int(f / m) - 1
                c += multi
                f -= multi * m
            else:
                f -= m
                c += 1
    return count(m, f, c)  # recursive call to test the next set of values for m and f


def solution(x, y):
    return count(x, y, 0)
