#http://usaco.org/index.php?page=viewproblem2&cpid=1229
from usaco_utils import *
from pprint import pprint as pp
from collections import defaultdict
"""
original test case => 1
5
2 0 0 1 0
3
5 2 3 4
2 1 1
3 1 2
----
5
2 1 1 3 1
3
5 2 3 4
2 1 1
3 1 2
------
6
2 0 0 1 1 0
4
5 2 3 4
2 1 1
3 1 2
6 2 1 5
"""


inputs = get_inputs("input.txt")
print(" Top ===== the inputs list ====")
pp(inputs)
print(" End ===== the inputs list ====")

n = int(inputs[0])
print("n: ", n)
nums = list(map(int, (inputs[1].split(" "))))
print("nums: ", nums)
k = int(inputs[2])
print(" k: ", k)

lmn=[]
recipes=defaultdict(set)
for ii in range(k):
    recipe=list(map(int,inputs[3+ii].split(" ")))
    print(" a recipe: ", recipe)
    recipes[recipe[0]]=set(recipe[2:])

print(" ===== recipes =====")
pp(recipes)


"""
# the golden rule => Bronze is all about trial and error
# find the max possible a.n -> try from 1... and continue to see if we can have all components
# in the recipe for a.n can be 1, if so, try 2, until we cannot get all true
"""

def is_nn_feasible(nums, idx, nn=0):
    print(" idx: ", idx, " nn: ", nn, " nums: ", nums)
    if idx==1: return nn <= nums[0]
    if nn<=0 or nn <= nums[idx-1]: return True
    if idx < 1: return False
    if idx not in recipes: return False

    #my_helper = lambda x: is_nn_feasible(nums, x, nn-nums[idx-1])
    #return all(list(map(my_helper, list(recipes.get(idx, [])))))

    nums_copy=nums[:]
    for r in recipes.get(idx, []):
        if is_nn_feasible(nums_copy, r, nn-nums_copy[idx-1]):
            nums_copy[r-1] -= (nn-nums_copy[idx-1]) #r alredy contributed the need, need to take out for all other components

        else:
            return False
    return True


def mxn():
    nn=0
    while is_nn_feasible(nums, n, nn):
        print(" nn okay => ", nn)
        nn += 1

    return nn-1

#print(mxn())

def mxn_binary():
    ll, rr = 0, 2*pow(10, 4)
    ans=-1
    while ll <= rr:
        mm=ll+(rr-ll)//2
        if is_nn_feasible(nums, n, mm):
            ans=mm
            ll=mm+1
        else:
            rr=mm-1

    return ans

print(mxn_binary())