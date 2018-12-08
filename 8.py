from collections import defaultdict

# get input as ints in a list
line = list(map(int, input().strip().split(' ')))

# debug print
def _print(*args):
    DEBUG = False
    if DEBUG:
        print(args)

# part 1
ans = 0
def process(line, index):
    global ans
    child_nodes      = line[0 + index]
    metadata_entries = line[1 + index]

    _print(f'no of child nodes: {child_nodes}')
    _print(f'no of metadata entries: {metadata_entries}')

    index += 2

    for _ in range(child_nodes):
        index = process(line, index)

    _print(f'index before reading metadata_entries: {index}')
    for i in range(metadata_entries):
        _print(f'{i + index}, adding: {line[index + i]}')
        ans += line[index + i]

    return index + metadata_entries

process(line, 0)
print(f'part 1: {ans}')

# part 2
def process_2(line, index, node_no, node_to_val):
    ans = 0
    child_nodes      = line[0 + index]
    metadata_entries = line[1 + index]

    _print(f'no of child nodes: {child_nodes}')
    _print(f'no of metadata entries: {metadata_entries}')

    index += 2

    child_node_no = 0
    # my_node_to_val will be enriched by my children
    my_node_to_val = defaultdict(int)
    for _ in range(child_nodes):
        child_node_no += 1
        index = process_2(line, index, child_node_no, my_node_to_val)

        
    for i in range(metadata_entries):
        metadata_entry = line[index + i]
        # if no child nodes, treat meta as vals
        if child_nodes == 0:
            ans += metadata_entry
        # treat meta as instead indexes
        else:
            ans += my_node_to_val[metadata_entry]

    # enrich my parent's dict
    node_name = chr(node_no + ord('A'))

    if node_name is 'A':
        print(f'part 2 ans: {ans}')

    _print(f'node_name: {node_name}')
    _print(f'my children: {my_node_to_val} and my ans: {ans}')

    node_to_val[node_no] = ans

    return index + metadata_entries

process_2(line, 0, 0, defaultdict(int))
