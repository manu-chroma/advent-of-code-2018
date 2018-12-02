import sys
import itertools
lines = sys.stdin.readlines() # i/o

# part 1
ans = sum(map(int, lines))
print(ans)

# part 2
record = {0}
ans = 0
for line in itertools.cycle(lines):
    ans += int(line)
    if ans in record:
        break
    
    record.add(ans)
print(ans)