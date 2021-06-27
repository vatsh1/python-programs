# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 14:11:25 2020

@author: shubh
"""
"""
r=open("D:\paglet.txt","r")
l=r.read()
print(l)
r.close()
"""
"""
with open("D:\paglet.txt","r") as f:
    last_line = f.readlines()
    l=1
    for line in last_line:
        print(str(l)+":- " + line)
        l = l+1
"""
"""
r=open("D:\ghora.txt","w")
r.write("what the fuck\n")
r.close()
"""
'''
inventory = {'apples':256,'bananas':564,'orange':210,'pears':110}
for cat in inventory.keys():
    print(cat,"has the value",inventory[cat])
'''
'''
import turtle
win = turtle.Screen()
shubh = turtle.Turtle()
shubh.shape('turtle')
y=13
for x in range(y):
    if x<=12:
        shubh.forward(50)
        shubh.right(30)
    else:
        y=y-12
        
'''
'''
def solution(data, n): // first question
    # Your code here
    p = 0
    d=[]
    for i in data:
        p = data.count(i)
        if(p<=n):
            d.append(i)
    return d
data=[1,2,2,2,3,4,5]
n = 1
print(solution(data,n))
            
'''
'''
def solution(l, t):
    length = len(l)
    i = 0
    while i < length:
        summ = 0
        while summ < t:
            for j in range(i, length, 1): // 2nd question
                summ = summ + l[j]
                #print (summ)
                if summ == t:
                    return i, j
 
 
        i += 1
    return -1, -1

l = [4, 3, 10, 2, 8]
t = 12
print(solution(l, t))
'''
'''
def getXOR(start, end):

    if (end - start) == 0:
        return 0
    if (end - start) == 1:      // 4th question
        return start
    if (end - start) <= 4:
        return reduce(lambda x, y: x ^ y, range(start, end))
    else:
        begin_range = (start, start / 4 * 4 + 4)
        end_range = (end / 4 * 4, end)
        return getXOR(*begin_range) ^ getXOR(*end_range)

def solution(start, length):
    # Your code here
    worker_list = [(start + (length - l) * length, start + (length - l) * length + l) for l in range(length, 0, -1)]
    
    new_xor = [getXOR(start, end) for start, end in worker_list]
    
    return reduce(lambda x, y: x ^ y, new_xor)

'''
'''
cnt=0
def divide(x):
    global cnt
    while(x>1):
        if (x & 1==0):
            #Dividing even number by two by shifting binary digits one step to the right.
            x=x>>1
        else:
            a=x+1
            b=x-1
            #counters ac & bc will be used to count trailing 0s // 5th question
            ac=bc=0
            #count trailing 0's for x+1
            while(a & 1==0):
                a=a>>1
                ac+=1
            #count trailing 0's for x-1
            while(b & 1==0):
                b=b>>1
                bc+=1
            #go with x+1 if it has more trailing 0s in binary format. Exception is number 3 as b10 can be divided in less steps than b100.
            #edge case 3 identified by manually testing numbers 1-10.
            if (ac>bc and x!=3):
                x+=1
            else:
                x-=1
        cnt+=1
def solution(n):
    # Your code here
    global cnt
    n=int(n)
    divide(n)
    return cnt
'''
'''
def solution(x, y):
    # Your code here
    X, Y = long(x), long(y)           //6TH QUESTION
    total = 0
    while not (X == 1 and Y == 1):
        if Y <= 0 or X <= 0:
            return "impossible"
        if Y == 1:
            return str(total + X - 1)
        else:
            total += long(X/Y)
            X, Y = Y, X % Y
    return str(total)

'''
'''
from itertools import combinations


def solution(num_buns, num_required):             //question 7// free the bunny prisioners
    keyrings = [[] for num in range(num_buns)]
    copies_per_key = num_buns - num_required + 1
    for key, bunnies in enumerate(combinations(range(num_buns), copies_per_key)):
        for bunny in bunnies:
            keyrings[bunny].append(key)

    return keyrings

'''
'''
import math

def commonFactor(x,y):
    if x == 0: return 'inf'
    if y == 0: return 0
    big = max(x,y)
    small = min(x,y)
    while(small!=0):
        r = small
        small = big % r
        big = r
    return abs(big)

def position(dimensions, your_position, guard_position,source):
    captains = []
    badguys = []
    width = dimensions[0]
    height = dimensions[1]
    cx = your_position[0]
    cy = your_position[1]
    gx = guard_position[0]
    gy = guard_position[1]
    for x,y in source[(0,0)]:
        captains.append((x,y))
        badguys.append((x+gx-cx,y+gy-cy))
    for x,y in source[(1,0)]:
        captains.append((x+width-2*cx,y))
        badguys.append((x+width-gx-cx,y+gy-cy))
    for x,y in source[(0,1)]:
        captains.append((x,y+height-2*cy))
        badguys.append((x+gx-cx,y+height-gy-cy))
    for x,y in source[(1,1)]:
        captains.append((x+width-2*cx,y + height-2*cy))
        badguys.append((x+width-gx-cx,y + height-gy-cy))
    return captains,badguys

def origin(dimensions, distance):
    sources = {}
    sources[(0,0)]=[]
    sources[(1,0)]=[]
    sources[(0,1)]=[]
    sources[(1,1)]=[]
    width = dimensions[0]
    height = dimensions[1]
    w = (distance/width) + 1
    h = (distance/height) + 1
    for x in range(-w,w+1):
        for y in range(-h,h+1):
            if x % 2 == y % 2:
                if x % 2 == 0:
                    sources[(0,0)].append((x*width,y*height))
                else:
                    sources[(1,1)].append((x*width,y*height))
            else:
                if x % 2 == 0:
                    sources[(0,1)].append((x*width,y*height))
                else:
                    sources[(1,0)].append((x*width,y*height))
    return sources

def countPossibilities(captain,badguy):
    global possibilities
    possibilities = {}
    for x,y in badguy:
        common = commonFactor(x,y)
        if common == 0:                                                    // 8th question bringing a gun to your guard wala
            if (0 not in possibilities or possibilities[0]>abs(x)):
                possibilities[0]= abs(x)
        elif common == 'inf':
            if ('inf' not in possibilities or possibilities['inf']>abs(y)):
                possibilities['inf']= abs(y)
        elif (x/common,y/common) not in possibilities or possibilities[(x/common,y/common)]>math.sqrt(x**2+y**2):
            possibilities[(x/common,y/common)]= math.sqrt(x**2+y**2)
    for x,y in captain:
        common = commonFactor(x,y)
        if common == 0:
            if 0 in possibilities and possibilities[0]>abs(x):
                del possibilities[0]
        elif common == 'inf':
            if 'inf' in possibilities and possibilities['inf']>abs(y):
                del possibilities['inf']
        elif (x/common,y/common) in possibilities and possibilities[(x/common,y/common)]>math.sqrt(x**2+y**2):
            del possibilities[(x/common,y/common)]
    return possibilities
def solution(dimensions, your_position, guard_position, distance):
    #Your code here
    origins = origin(dimensions, distance)
    captain,badguy = position(dimensions, your_position, guard_position,origins)
    captain = [x for x in captain if math.sqrt(x[0]**2+x[1]**2) <= distance and not (x[0]==x[1]==0)]
    badguy = [x for x in badguy if math.sqrt(x[0]**2+x[1]**2) <= distance and not (x[0]==x[1]==0)]
    possibilities = countPossibilities(captain,badguy)
    return len(possibilities)
    
'''
'''
def generate(c1,c2,bitlen):
    a = c1 & ~(1<<bitlen)
    b = c2 & ~(1<<bitlen)
    c = c1 >> 1
    d = c2 >> 1
    return (a&~b&~c&~d) | (~a&b&~c&~d) | (~a&~b&c&~d) | (~a&~b&~c&d)

from collections import defaultdict
def build_map(n, nums):
    mapping = defaultdict(set)
    nums = set(nums)
    for i in range(1<<(n+1)):
        for j in range(1<<(n+1)):
            generation = generate(i,j,n)
            if generation in nums:
                mapping[(generation, i)].add(j)               // question 9 escaped nudles
    return mapping
def solution(g):
    # Your code here
    g = list(zip(*g)) # transpose
    nrows = len(g)
    ncols = len(g[0])

    # turn map into numbers
    nums = [sum([1<<i if col else 0 for i, col in enumerate(row)]) for row in g]
    mapping = build_map(ncols, nums)

    preimage = {i: 1 for i in range(1<<(ncols+1))}
    for row in nums:
        next_row = defaultdict(int)
        for c1 in preimage:
            for c2 in mapping[(row, c1)]:
                next_row[c2] += preimage[c1]
        preimage = next_row
    ret = sum(preimage.values())

    return ret
    
'''






































        
        
        
        
        
        
        
        
        