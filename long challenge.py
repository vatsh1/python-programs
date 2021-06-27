# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 16:38:12 2020
if b not in s:
            if r[f]< r[b[0]]:
                s.append(f)
                n=n+1
            elif f=='a':
                s.append(f)
                n = n+ 1
            else:
                s.append(b)
                s.append(f)
                n = n+1
        else:
            s.append(f)
            n = n+1
@author: shubh
"""

def minDiff(arr):
    ans=0
    arr.sort()
    for i in range(1,len(arr)):
        ans+=arr[i]-arr[i-1]
    return ans
    
n = int(input())
k = list(map(int,input().split()))[:n]
print(minDiff(k))