# modify this function, and create other functions below as you wish
def question04(v, c, mc):
    if len(v) == 0 or len(c) == 0:
        return 0
    if len(v) != len(c):
        return 0
    answer = 0
    maxc = max(c)
    minc = min(c)
    # print(maxc)
    while mc >= minc:
        if maxc <= mc:
            index = c.index(maxc)
            # print(index)
            mc -= maxc
            # print(mc)
            answer += v[index]
            v[index] = 0
            c[index] = 0
            maxc = max(c)
            # print (mc)
        else:
            index = c.index(maxc)
            v[index] = 0
            c[index] = 0
            maxc = max(c)
    return answer


if __name__ == '__main__':
    print(question04([6, 10, 12], [30, 70, 90], 30))
