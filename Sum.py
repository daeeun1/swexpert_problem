for test in range(1, 11):
    test_case = int(input())
    d = []
    for i in range(100):
        d.append(list(map(int, input().split())))

    answer = 0
    r_under = 0
    l_under = 0
    for i in range(100):
        #가로
        if sum(d[i]) > answer:
            answer = sum(d[i])
        #세로
        low_sum = 0
        for j in range(100):
            low_sum += d[j][i]
        if low_sum > answer :
            answer = low_sum

        #우 아래 대각
        r_under += d[i][i]

        #좌 아래 대각
        l_under = d[99-i][i]

        answer = max(answer, r_under, l_under)
    print("#%d %d" %(test_case, answer))