import sys
lines = sys.stdin.readlines() # i/o

# array bounds
MAX = int(1e2)
arr = [[0 for _ in range(MAX)] for _ in range(MAX)]

# states variables for part 2 
not_pristine = set()
prev_marked  = [[-1 for _ in range(MAX)] for _ in range(MAX)]
pristine = True

for line in lines:
    # input parse
    line   = line.split(' ')
    offset = tuple(map(int, line[2].strip(':').split(',')))
    dims   = tuple(map(int, line[3].strip().split('x')))
    claim  = int(line[0][1:])

    pristine = True

    for x in range(offset[0], offset[0] + dims[0]):
        for y in range(offset[1], offset[1] + dims[1]):

            # array bounds check
            assert x <= MAX and y <= MAX, f'x: {x} and y: {y}'
            
            # already someone is there
            if arr[x][y] != 0:
                pristine = False
                # add previous one if not present
                if prev_marked[x][y] not in not_pristine:
                    not_pristine.add(prev_marked[x][y])

            prev_marked[x][y] = claim
            arr[x][y] += 1

    if not pristine:
        not_pristine.add(claim)


# part 1
# calculate count
ans = 0
for x in range(0, MAX):
        for y in range(0, MAX):
            if arr[x][y] >= 2:
                ans += 1
print(ans)

# part 2 ans
all_id_set = set([i for i in range(1, len(lines) + 1)])
print(all_id_set - not_pristine)