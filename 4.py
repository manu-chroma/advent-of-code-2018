import sys
lines = sys.stdin.readlines() # i/o
lines = [line.strip() for line in lines]

# debug print
def _print(*args):
    debug = False
    if debug:
        print(*args)


# part 1

# sort the input in chronological order
lines = sorted(lines, key=lambda x: x.split(']')[0]) # key is the timestamp here

# state variables
prev_time_minutes = None
prev_id = None
prev_date = None
gid = None # guard id
prev_state = 'begin' # 'begin', 'sleep', 'awake'

gaurd_sleep = {}
gaurd_minute_tracking = {}

def update_gaurd_minutes(gid, min_start, min_end):
    """update state dicts for sleeping start and end time
    for a given gaurd id"""
    
    time_slept = min_end - min_start
    # update cumulative time
    if gaurd_sleep.get(gid) is None:
        gaurd_sleep[gid] = time_slept
    else:
        gaurd_sleep[gid] += time_slept

    # update per minute tracking
    if gaurd_minute_tracking.get(gid) is None:
        gaurd_minute_tracking[gid] = [0 for i in range(0, 60)]
    
    for minute in range(min_start, min_end + 1):
        gaurd_minute_tracking[gid][minute] += 1

for line in lines:
    # boring(bad) i/o parsing
    # use regex instead
    line = line.split(' ')
    date = line[0].split('[')[1]
    time = line[1].split(']')[0]
    time_min = int(time.split(':')[1])

    _print(line)

    keyword = line[2]
    
    # new gaurd incoming
    if keyword == 'Guard':
        # update previous and
        # assign new gaurd id from input 
        prev_id = gid
        gid = int(line[3][1:])

        _print(f'new gaurd incoming: {gid}')

        # only if previous state was sleeping
        # do we need to add this on new guard incoming
        # NOTE: won't come here if prev_gid is None
        if prev_state == 'sleep':
            _print(f'prev_time: {prev_time_minutes}')
            update_gaurd_minutes(prev_id, prev_time_minutes, 59)
        # reset state
        prev_state = 'awake'

    # update status
    elif keyword == 'wakes':
        _print(f'prev_time: {prev_time_minutes}')
        # if keyword is 'wakes'
        # then gaurd is sleeping for sometime
        update_gaurd_minutes(gid, prev_time_minutes, time_min)
        prev_state = 'awake'
        
    elif keyword == 'falls':
        # do for previous
        if prev_state is 'sleep':
            update_gaurd_minutes(gid, prev_time_minutes, 59)

        # update previous time
        prev_time_minutes = time_min
        prev_state = 'sleep'

# ans
max_minutes = max(gaurd_sleep.values())
max_gaurd = None

for k, v in gaurd_sleep.items():
    if v == max_minutes:
        max_gaurd = k

max_minutes = gaurd_minute_tracking[max_gaurd].index(
    max(gaurd_minute_tracking[max_gaurd]))
print(f'most sleeping gaurd: #{max_gaurd} and max slept minute: {max_minutes}')
print(f'Part 1 ans: {max_gaurd * max_minutes}')

# part 2
max_minutes_global = None
max_min_count = -1
gid_max = None
for k, v in gaurd_minute_tracking.items():
    tmp = max(gaurd_minute_tracking[k])
    if tmp > max_min_count:
        max_min_count = tmp
        max_minutes_global = gaurd_minute_tracking[k].index(tmp)
        gid_max = k

print(f'gaurd #{gid_max} was asleep most on a given minute, which is {max_minutes_global} with frequency: {max_min_count}')
print(f'Part 2 ans: {gid_max * max_minutes_global}')