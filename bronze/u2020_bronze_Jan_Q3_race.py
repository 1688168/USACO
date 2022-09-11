"""
Objective: to finish the distance K in  min time
Idea: what's the max speed we can go to finish distance K with ending speed less than or equal to X
* min feasible speed: 1
* max possible speed: K (although we know this is not feasible, but we know this is the upper bound, or we can use max(k)=10^9 as upper bound)
* we know speed space     [1, 2, ... 10^9]
  we know feasible space  will be like [T, T, T, F, F,...F]. ie at some point, the max speed is NOT feasible
  => this is a binary search patter

strategy:
1. implement a is_feasible_max_speed function: given a max speed, can we finish K with max_ending_speed X.
++ need to be able to increase speed to the target max_speed, and decrease speed to be less than or eaual to X.

2. binary search the max_feasible_speed.
3. based on the max_feasible_speed calculate the required time.


Idea: by simulation
* on each step, consider if this speed is too fast or too slow. if too fast, reduce speed, else increase
"""
from usaco_utils import *
from pprint import pprint as pp


inputs = get_inputs("input.txt")

kk, nn = map(int, inputs[0].split())

def get_min_time_reach_k(s, k, x):
    dist_so_far=0
    t=0 #time used
    while dist_so_far < k:
        t += 1

        # can we increase speed
        if (dist_so_far + ((s+1)+x)*(s+1-x+1)//2) <= k+x-1: # if we can bring down speed before reaching k => we can go s+1 on this iteration
            s += 1
        else: # we cannot increase speed, should we reduce speed?
            if s > x and (dist_so_far + (s+x)*(s-x+1)//2) >= k+x: # can I maintain same speed
                s -= 1
        dist_so_far += s
        print("(t, s, d) = (" + str(t) +", "+ str(s) + ", "+ str(dist_so_far) +")")

    return t


for ii in range(nn): #run each x
    print(get_min_time_reach_k(0, kk, int(inputs[ii+1])))

"""
-- original
6
E 3 5
N 5 3
E 4 6
E 10 4
N 11 2
N 8 1

-- test 1
7
E 3 5
N 5 3
E 4 6
E 10 4
N 11 2
N 8 1
E 1 10
"""