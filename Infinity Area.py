import math
from xml.etree.ElementTree import TreeBuilder

from numpy import arange

T=int(input())
for i in range(T):
    R,A,B=map(int,input().split())

    area=math.pi * (R*R)
    while R!=0:
        R=R*A
        area+=math.pi * (R*R)
        R=R//B
        area+=math.pi * (R*R)
    print(f"Case #{i+1}: {'%.6f' %area}")




