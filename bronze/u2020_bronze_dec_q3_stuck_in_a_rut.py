#http://usaco.org/index.php?page=viewproblem2&cpid=1061

from usaco_utils import *
from pprint import pprint as pp
from collections import deque

inputs = get_inputs("input.txt")
print("----- inputs ----- top")
pp(inputs)
print("----- inputs ----- end")

# num of cows:
n=int(inputs[0])

cow_state={}
dq=deque()
n_cnt=0
e_cnt=0
max_x=-1
max_y=-1

for ii in range(n):
    a_cow_info=inputs[1+ii].split(" ")
    x=int(a_cow_info[1])
    y=int(a_cow_info[2])
    dir=a_cow_info[0]
    if dir == 'N':
        n_cnt += 1
        max_x=max(max_x, x)
    else:
        e_cnt += 1
        max_y=max(max_y, y)
    dq.append((dir, x, y, ii))
    cow_state[(x,y)]=0

print("----- initial state -----")
pp([x for x in dq])
print(" n_cnt: ", n_cnt, ' e_cnt: ', e_cnt, ' max_x: ', max_x, ' max_y', max_y)


def has_no_potential_collision(d, cx, cy, dq):
    for (dir, x, y, idx) in dq:
        if d=='N':
            if dir == 'E' and x < cx and y > cy: return False
        else:
            if dir == 'N' and x > cx and y < cy: return False
    return True


tt = 0
res=['infinity' for _ in range(n)]
while (sz := len(dq)) > 0:
    tt += 1 #after 1 hour
    print(" =========== sz: ", sz, " =============")

    while sz > 0:
        (d, x, y, idx) = dq.popleft()
        sz -= 1
        if d=='N':
            nx=x
            ny=y+1
        else:
            nx=x+1
            ny=y


        if (nx, ny) in cow_state and tt > cow_state[(nx, ny)]: #location is eaten before tt
            print(idx, " stopping as (", nx,",", ny,") is eaten")
            res[idx]=tt
        elif d=='N' and ny >= max_y:
            cow_state[(nx, ny)] = tt
            print(idx, " getting out of max_y -> I am free go N!")
            #pass # infinity
        elif d=='E' and nx >= max_x:
            cow_state[(nx, ny)] = tt
            print(idx, " getting out of max_x -> I am free go E!")

        elif d=='E' and has_no_potential_collision('E', x, y, dq):
            cow_state[(nx, ny)] = tt
            print(idx, " getting out due to no potential collision ==> I am a free E")
        elif d=='N' and has_no_potential_collision('N', x, y, dq):
            cow_state[(nx, ny)] = tt
            print(idx, " getting out due to no potential collision ==> I am a free N")
        else: # continue
            dq.append((d, nx, ny, idx))
            cow_state[(nx, ny)] = tt

    # border condition check
    # if all cows on same direction, no need to check further
    if n_cnt==0 or e_cnt==0:
        print(" single direction left, get out")
        break


    print("# == tt: ", tt, " == ")
    pp([x for x in dq])
    pp(cow_state)
    pp(res)

print(" ===== final ===== ")
print(res)

"""
-- original
6
E 3 5
N 5 3
E 4 6
E 10 4
N 11 2
N 8 1

---
7
E 3 5
N 5 3
E 4 6
E 10 4
N 11 2
N 8 1
E 1 10

---
8
E 3 5
N 5 3
E 4 6
E 10 4
N 11 2
N 8 1
E 1 10
E 9 1

---
9
E 3 5
N 5 3
E 4 6
E 10 4
N 11 2
N 8 1
E 1 10
E 9 1
E 7 3

--
11
E 3 5
N 5 3
E 4 6
E 10 4
N 11 2
N 8 1
E 1 10
E 9 1
E 7 3
N 20 2
E 11 12
---
1
E 3
"""