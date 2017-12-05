#!/usr/bin/env python3

a = 347991
s = 591

brc = s * s
blc = brc - (s - 1)
tlc = blc - (s - 1)
trc = tlc - (s - 1)
mid = (trc + tlc) / 2
h = a - mid
v = (s - 1) / 2
print(v + h)

# part 2
# https://oeis.org/A141481
