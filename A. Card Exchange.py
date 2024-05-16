for _ in range(int(input())):
    lnk = [int(_) for _ in input().split(" ")]
    ln ,k = lnk[0] , lnk[1]
    arr : list[int] = [int(_) for _ in input().split(" ")]
    if ln < k :
        print(ln)
    else:
        uniqueLs = set(arr)

        if (ln == len(uniqueLs)) :
            print(ln)
        elif k > max([arr.count(_) for _ in uniqueLs]):
             print(ln)
        else :
            print(k-1)