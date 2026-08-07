L = [1, 2, 3, 4, 5]
print(L)
count = 0
for i in L:
    count += i

average = count / len(L)
print("sum =", count)
print("average =", average)

L.sort()

print("smallest element is", L[0])
print("largest element is", L[-1])