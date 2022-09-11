#http://usaco.org/index.php?page=viewproblem2&cpid=1036

import os, sys
from pprint import pprint as pp
input_file= os.path.join(os.getcwd(), 'u2020_bronze_March_q2_input.txt')

cows = []
with open(input_file, mode='r', encoding="utf-8") as f:
    n = int(f.readline()) # number of lines
    print(" numOfNums: ", n)

    for ii in range(n):
         idx, is_sick = f.readline().split()
         cows.append((int(idx), int(is_sick)))
cows.sort()
pp(cows)

# find the R
#prev_healthy_dist = [0]*n

# if n=1, we know at least one cow sick ---> return 1
if n==1:
    print(1)
    exit(0)


sick_cow_cnt=0
prev_sick_dist = [0]*n
prev_sick_dist[0] = 0 if cows[0][1] == 1 else float('inf')
if cows[0][1]==1: sick_cow_cnt += 1
for ii in range(1, n):
    prev_sick_dist[ii] = 0 if cows[ii][1]==1 else (cows[ii][0] - cows[ii-1][0]+prev_sick_dist[ii-1])

    if cows[ii][1] == 1:
        sick_cow_cnt += 1

# if only one cow sick -> return 1
if sick_cow_cnt == 1:
    print(1)
    exit(0)


# if all cows sick => unable to determine R -> R is inf -> one group is enough

if sick_cow_cnt == n:
    print(1)
    exit(0)

print("dist array to prev sick cow")
pp(prev_sick_dist)

#next_healthy_dist = [0]*n
next_sick_dist = [0]*n
next_sick_dist[n-1] = 0 if cows[n-1][1] == 1 else float('inf')
for ii in reversed(range(0,n-1)):
    next_sick_dist[ii] = 0 if cows[ii][1] == 1 else ( cows[ii+1][0]+prev_sick_dist[ii+1] - cows[ii][0] )

print("dist array to next sick cow")
pp(next_sick_dist)


print(" --- identifying R ---")
r=pow(10, 6)
for ii in range(n):
    if(cows[ii][1]==0):
        r=min(r, prev_sick_dist[ii], next_sick_dist[ii])

print("r: ", r)


#find the first sick cow
for jj in range(n):
    if cows[jj][1]==1:
        break

print(" the first sick cow location: ", jj)
num_of_group = 1

prev_sick_idx=jj
for ii in range(jj+1, n):
    if cows[ii][1]==1 and cows[ii][0]-cows[prev_sick_idx][0] >= r:
        num_of_group += 1

    if cows[ii][1]==1:
        prev_sick_idx=ii

print(" num of groups: ", num_of_group)




# test cases, if only 1 cow sick -> 1


