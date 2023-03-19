def op(i, n, mas, swaps):
    min_indek = i
    l = 2*i + 1
    if l < n and mas[l] < mas[min_indek]:
        min_indek = l
    r = 2*i + 2
    if r < n and mas[r] < mas[min_indek]:
        min_indek = r
    if i != min_indek:
        swaps.append((i, min_indek))
        mas[i], mas[min_indek] = mas[min_indek], mas[i]
        op(min_indek, n, mas, swaps)

def into_heap(mas):
    n = len(mas)
    swaps = []
    for i in range(n//2, -1, -1):
        op(i, n, mas, swaps)
    return swaps

n = (input())
mas = list(map(int, input().split()))
swaps = into_heap(mas)

print(len(swaps))
for swap in swaps:
    print(swap[0], swap[1])
