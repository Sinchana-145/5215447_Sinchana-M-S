import sys

q = int(sys.stdin.readline().strip())
S = ""
stk = []

for _ in range(q):
    portions = sys.stdin.readline().strip().split()
    op = int(portions[0])

    if op == 1:
        w = portions[1]
        stk.append(("1", len(w)))
        S += w
    elif op == 2:
        k = int(portions[1])
        delt = S[-k:]
        stk.append(("2", delt))
        S = S[:-k]
    elif op == 3:
        k = int(portions[1])
        print(S[k-1])
    elif op == 4:
        last = stk.pop()
        if last[0] == "1":
            length = last[1]
            S = S[:-length]
        else:
            S += last[1]