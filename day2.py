import sys
lines = sys.stdin.readlines() # i/o

# pre-process
lines = [line.strip() for line in lines]

# part 1
twos, threes = 0, 0

for line in lines:
    counter = {}

    for _ in line:
        if counter.get(_) is None:
            counter[_] = 1
        else:
            counter[_] += 1

    twos   += 1 if 2 in counter.values() else 0
    threes += 1 if 3 in counter.values() else 0

print(twos * threes)
    
# part 2
def lines_diff(l1, l2):
    ans = 0
    for ch, ch2 in zip(l1, l2):
        if ch != ch2:
            ans += 1
    return ans

ans = ''
found = False
for l1 in lines:
    for l2 in lines:

        if l1 == l2 or len(l1) != len(l2):
            continue

        if lines_diff(l1, l2) == 1:
            ans_list = [i for i, j in zip(l1, l2) if i == j ]
            ans = ''.join(ans_list)
            found = True
            break

    if found is True:
        break

assert(found is True)
print(ans)