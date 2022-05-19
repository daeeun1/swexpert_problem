for test in range(1, 11):
    n = int(input())
    d_row = [[None] * 8 for i in range(8)]
    d_low = [[None] * 8 for i in range(8)]
    for i in range(8):
        a = input()
        for j in range(8):
            d_row[i][j] = a[j]

    for i in range(8):
        for j in range(8):
            d_low[i][j] = d_row[j][i]
    count = 0
    for i in range(8):
        for j in range(8 - n + 1):
            A = d_low[i][j:j + n]

            if A == A[::-1]:
                count += 1

        for j in range(8 - n + 1):
            A = d_row[i][j:j + n]

            if A == A[::-1]:
                count += 1
    print("#%d %d" %(test, count))