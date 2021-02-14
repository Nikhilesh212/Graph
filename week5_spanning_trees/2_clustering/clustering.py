#Uses python3
import sys
import math

class disjoint:
    def __init__(self,n):
        self.rank=[1]*n
        self.parent=[i for i in range(n)]
    def find(self,i):
        while self.parent[i]!=i:
            i=self.parent[i]
        return i
    def union(self,i,j):
        seti=self.find(i)
        setj=self.find(j)
        if seti!=setj:
            if self.rank[seti]>self.rank
