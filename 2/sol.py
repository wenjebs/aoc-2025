# comma separated ranges
# for  each ranges find the sum of invalid ids
# invalid ids are ids that have a repeated sequence twice, e.g 55, 123123, 12341234.

# how do u check if a id has two repeated sequences?
# 1-> check the len, if odd then impossible
# 2-> even -> check if firest half = second half 

# this takes in a string
def is_invalid(id):
    if len(id) % 2 != 0:
        return False
    first_half = id[:len(id)//2]
    second_half = id[len(id)//2:]
    if first_half == second_half:
        return True
    return False

def solve(input):
    # split by comma
    ranges = input.split(',')
    sol = 0
    # for each range
    for range_str in ranges:
        start, end = range_str.split('-')
        # print(type(start), type(end))
        for id in range(int(start), int(end)+1):
            if is_invalid(str(id)):
                sol += id
    return sol
# print(open('input.txt', 'r').read())
print(solve(open('input.txt', 'r').read().strip()))
