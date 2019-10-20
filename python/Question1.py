# modify this function, and create other functions below as you wish
def question01(initialLevelOfDebt, interestPercentage, repaymentPercentage):

    answer = 0
    if interestPercentage >= repaymentPercentage:
        return 0
    if initialLevelOfDebt == 0:
        return 0
    totalDebt = initialLevelOfDebt
    # print("total Debt: ", totalDebt)
    # print(initialLevelOfDebt * (repaymentPercentage / 100))
    repayment = initialLevelOfDebt * (repaymentPercentage / 100.0)
    answer += (initialLevelOfDebt * 0.1)

    while totalDebt > 0:
        # interest = totalDebt * (interestPercentage / 100.0)
        totalDebt += (totalDebt * (interestPercentage / 100.0))
        if repayment < 50:
            repayment = 50
        # totalDebt -= repayment
        if totalDebt - repayment > 0:
            totalDebt -= repayment
        else:
            repayment = totalDebt
            totalDebt = 0
        # print("totaldebt",totalDebt)
        # print("rep",repayment)
        answer += repayment
        # print("answer", answer)
        # answer += totalDebt
        if totalDebt <= 50:
            answer += totalDebt
            totalDebt = 0

    return answer


if __name__ == '__main__':
    print(question01(1000, 10, 20))