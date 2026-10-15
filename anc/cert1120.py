#!/usr/bin/env python3
"""Independent exact recomputation of the mass certificate for the Harman
4-level tree at T=9/20 (z=X^{1/10}).  Fraction arithmetic only."""
from fractions import Fraction as F
from math import factorial
import sys
T=F(9,20); d=1-2*T; h=1-T; C=F(71,125)
assert d==F(1,10) and h==F(11,20)
def wbar(u0):
    if u0<1: return F(1)
    return max(1/u0, C)
# Buchstab constant
assert C*sum(C**j/factorial(j) for j in range(5))>1
# U2 cover n=256
n=256; H=(T-d)/n; U2=F(0); cu=0
for ib in range(n):
    b0=d+ib*H; b1=b0+H
    for ia in range(ib,n):
        a0=d+ia*H; a1=a0+H
        if a0>=T or a1+b1<=h or a0+2*b0>1: continue
        U2+=wbar((1-a1-b1)/b1)/(a0*b0*b0)*H*H; cu+=1
# V4 cover n=64
n=64; H=(T-d)/n; V4=F(0); cv=0
for ia in range(n):
  a0=d+ia*H; a1=a0+H
  for ib in range(ia+1):
    b0=d+ib*H; b1=b0+H
    if a0+b0>=T: continue
    for ic in range(ib+1):
      c0=d+ic*H; c1=c0+H
      if a1+b1+c1<=h: continue
      for ie in range(ic+1):
        e0=d+ie*H; e1=e0+H
        if a0+b0+c0+2*e0>1: continue
        V4+=H**4*wbar((1-a1-b1-c1-e1)/e1)/(a0*b0*c0*e0*e0); cv+=1
x=7*T-3; y=9*T-4
L4=C*y**4/(576*d**5); U4=C*x**4/(1728*d**5)
U2r=F(732661466777,10**12); V4r=F(98012508379,10**12)
c=1-U2r-L4-U4-V4r
print("U2 cells",cu,"U2 exact ~ %.16f"%float(U2),"<= rounded",U2<=U2r, "gap",float(U2r-U2))
print("V4 cubes",cv,"V4 exact ~ %.16f"%float(V4),"<= rounded",V4<=V4r, "gap",float(V4r-V4))
print("L4",L4,"U4",U4)
print("c_cert",c,"= %.18f"%float(c), c==F(342155430899,2250000000000))
print("c_cert unrounded ~ %.18f"%float(1-U2-L4-U4-V4))
print("1.32*c/8 =",float(F(132,100)*c/8))
print("U2 exact den digits",len(str(U2.denominator)),"V4 den digits",len(str(V4.denominator)))
