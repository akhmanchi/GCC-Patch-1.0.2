# modify this function, and create other functions below as you wish
def question02(risk, bonus, trader):
    answer = 0
    if not (len(risk) or range(1, 10001) or len(bonus) in range(1, 10001) or len(trader) in range(1, 10001)):
        return 0
    if len(risk) != len(bonus):
        return 0
    for t in range(len(trader)):
        max = 0
        for r in range(len(risk)):
            if trader[t] >= risk[r]:
                if bonus[r] > max:
                    max = bonus[r]
        # print(max)
        answer += max
    return answer


if __name__ == '__main__':
    print(question02([9, 1, 1, 6, 1], [9, 9, 8, 10, 20], [2, 10, 9, 10, 10, 7, 9]))
