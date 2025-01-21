import sys

output = []

while True:
    a, b, c = map(int, sys.stdin.readline().split())

    if a == 0 and b == 0 and c == 0:
        break

    if a == b == c:
        output.append("Equilateral")
    elif a == b:
        if c >= a + b:
            output.append("Invalid")
        else:
            output.append("Isosceles")
    elif b == c:
        if a >= b + c:
            output.append("Invalid")
        else:
            output.append("Isosceles")
    elif c == a:
        if b >= a + c:
            output.append("Invalid")
        else:
            output.append("Isosceles")
    else:
        if a + b <= c or a + c <= b or b + c <= a:
            output.append("Invalid")
        else:
            output.append("Scalene")

for str in output:
    print(str)