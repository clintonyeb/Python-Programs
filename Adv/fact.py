def findFact(n):
    res = list()
    for i in range(1, n+1):
        if (n % i) == 0:
            print('adding', i)
            res.append(i)
    return res

