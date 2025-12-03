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

# def solve(input):
#     # split by comma
#     ranges = input.split(',')
#     sol = 0
#     # for each range
#     for range_str in ranges:
#         start, end = range_str.split('-')
#         # print(type(start), type(end))
#         for id in range(int(start), int(end)+1):
#             if is_invalid(str(id)):
#                 sol += id
#     return sol
# print(open('input.txt', 'r').read())
# print(solve(open('input.txt', 'r').read().strip()))


# now an invalid id is defined as one that has a repeated sequence AT LEAST twice, so it could be more
# e.g 11, 123123123, 1111111, 123412341234, etc.
# even is ok now, cause can be 3 1's or sth liek that
#  use an expanding sliding window 
# left pointer and right pointer
# right pointer goes thru the string
# left pointer stays at the start
# kepe track of seen digits, if sth seen appears, e.g for 123123, we see 123, then 1, then we know len of window is 3, then we check from left + 3 to right if the sequence is repeated until the end of the string
def is_invalid2(id):
    left = 0
    right = 0
    seen = set()
    window_len = 0

    # find a window length with a repeated sequence by expanding window till seeing a seen number then keeping the window length
    while right < len(id):
        if id[right] in seen:
            window_len = right - left
            break
        seen.add(id[right])
        right += 1

    # no repeated sequence was found
    if window_len == 0:
        return False
    # check if the window length is repeated
    for i in range(0, len(id) - window_len, window_len):
        if id[i:i+window_len] != id[i+window_len:i+2*window_len]:
            return False
    return True

def solve2(input):
    # split by comma
    ranges = input.split(',')
    sol = 0
    # for each range
    for range_str in ranges:
        start, end = range_str.split('-')
        # print(type(start), type(end))
        for id in range(int(start), int(end)+1):
            if is_invalid2(str(id)):
                print(id)
                sol += int(id)
    return sol
# print(open('input.txt', 'r').read())
print(solve2(open('input.txt', 'r').read().strip()))