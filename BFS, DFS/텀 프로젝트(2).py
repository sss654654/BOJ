T = int(input())

while T != 0:
    if T < 0:
        break
    T -= 1
    n = int(input())
    selpart = [int(x) for x in input().split()]
    selpart.insert(0, 0)
    group = []
    # [1,3] [2,1] [3,3] [4,7] [5,3] [6,4] [7,6]
    for i in range(1, n+1):
        group.append([i, selpart[i]])

    groupcount = 0

    temp = []
    templist = []

    for li in group:
        # i = [1,3] -> [2,1] ...
        temp.append(group[li[1] - 1])  # i[1] = 3 -> group[2]
        while True:  # [4,7]일 경우 temp에는 [7,6] 가 들어감
            if templist == temp[0] and li[0] != templist[1]:
                # 그룹이 성사되지 않고 무한 반복될 경우
                # print("fail : {} , {}".format(li, templist))
                temp.clear()
                break
            templist = temp.pop(0)
            if li[0] == templist[1]:  # i[1,3] == temp[3,3] 1 == 3
                # print("clear : {} , {}".format(li, templist))
                groupcount += 1
                break
            temp.append(group[templist[1] - 1])
            # temp가 [7,6]이고 다시 temp에는 [6,4]가 담김

    print(n-groupcount)
