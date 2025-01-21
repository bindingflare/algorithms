import sys
import math

N, M, a, b = map(int, sys.stdin.readline().split())

h = math.ceil(N / (a + 1))
w = math.ceil(M / (b + 1))

print(h * w)