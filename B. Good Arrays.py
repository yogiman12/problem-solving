n = int(input())

for _ in range(n):
    ln = int(input())
    arr : list[int] = [int(_) for _ in input().split(" ")]
    sm = sum(arr)
    cnt_one = arr.count(1)
    if all(arr):
        if ln <= 1 :
            print('no')
        elif (cnt_one > ln/2) &( sm-cnt_one <ln) :
            print('no') 
        else : print('yes')       
        
    else:
        print('no') 