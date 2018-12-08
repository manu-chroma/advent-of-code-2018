import sys
from functools import reduce
line = sys.stdin.read() # i/o only single line in input

line = list(line.strip())

# part 1
# NOTE: brute force, memory unoptimised too
def part1(line):
    while 1:
        found = False
        i = 1

        assert(-1 not in line)

        while i < len(line):
            if abs(ord(line[i-1]) - ord(line[i])) == 32:
                line[i-1] = line[i] = -1
                found = True
                i += 2
            else:
                i += 1

        # cleanup all the -1 from the list
        line = [i for i in line if i != -1]

        if not found:
            break

    return line

line = part1(line)
ans = len(line)
print(ans)

# part 2
# re-using line from previous ans
set_of_letters = set([i.lower() for i in line])

for i in set_of_letters:
    # create new line
    new_list = [x for x in line if x.lower() != i]
    new_ans = len(part1(new_list))
    if new_ans < ans:
        ans = new_ans
print(ans)
