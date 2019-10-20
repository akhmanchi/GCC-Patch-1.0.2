# modify this function, and create other functions below as you wish
def question03(scores, alice):
    if len(scores) == 0 and len(alice) == 0:
        return 0
    totalScore = scores + alice
    totalScore.sort(reverse=True)
    totalRank = []
    myRank = []

    totalRank.append(1)

    for r in range(len(totalScore)-1):
        if totalScore[r] == totalScore[r+1]:
            totalRank.append(totalRank[r])
        else:
            totalRank.append(totalRank[r]+1)

    for i in range(len(alice)):
        myRank.append(totalRank[totalScore.index(alice[i])])
    myRank.sort()

    answer = max(set(myRank), key=myRank.count)

    return answer


if __name__ == '__main__':
    print(question03([100, 90, 90, 80, 75, 60], [50, 77, 78, 90]))
