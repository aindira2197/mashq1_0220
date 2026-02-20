# 1
n = int(input())
for i in range(1, n + 1):
    print("*" * i)

# 2
n = int(input())
for i in range(n, 0, -1):
    print("#" * i)

# 3
n = int(input())
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)

# 4
n = int(input())
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# 5
n = int(input())
for i in range(n):
    print("*" * n)
