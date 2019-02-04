
n = int(raw_input())
a = [int(raw_input()) for _ in range(n)]
#arr = map(int, raw_input().split())

r = list(set(a))

for i in range(0,len(r) - 1):
    for j in range(0,len(r) - i - 1):
        if r[j] < r[j + 1]:
            temp = r[j]
            r[j] = r[j + 1]
            r[j + 1] = temp

print r[1], r


# optimization required for the above code
