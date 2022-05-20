def solve (N, Current, Desired):
    # Write your code here
    moves = 0
    elem = [0]*len(Current)
    if Current == Desired:
        return 0
    
    for i in range(1,len(Current)):
        if Current[i] == Desired[i]:
            continue
        else:
            if elem[i] == 0:
                if Current[i] == Desired[i-1]:
                    Current[i], Current[i-1] = Current[i-1], Current[i]
                    moves+=1
                    elem[i]+=1
                    elem[i-1]+=1
                elif Current[i] == Desired[i+1]:
                    Current[i], Current[i+1] = Current[i+1], Current[i]
                    moves+=1
                    elem[i]+=1
                    elem[i+1]+=1
    print(Current)
    if Current != Desired:
        return -1
    else:
        return moves

T = int(input())
for _ in range(T):
    N = int(input())
    Current = list(map(int, input().split()))
    Desired = list(map(int, input().split()))

    out_ = solve(N, Current, Desired)
    print (out_)