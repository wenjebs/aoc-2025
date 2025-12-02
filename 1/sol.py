# count num of times we hit 0 at every rotation

# dial starts at 50
# dial goes from 0 - 99
# if sum > 99, then go to 0 and add the rest
# if sum < 0 then go to 99 and subtract the rest
# we can mod 100 to get the new position since circular
# loop thru each input, calc final position -> if 0 then +=1 , else continue
# 97 98 99 0 1 2, actual pos = final pos 100 - current pos
# 98 , r5 -> 99 , 0, 1, 2, 3 -> final pos - 100 = actual pos
current_position = 50
sol = 0
with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if line.startswith('L'):
            current_position -= (int(line[1:]) % 100)
        elif line.startswith('R'):
            current_position += (int(line[1:]) % 100)

        if current_position < 0:
            current_position = 99 + (current_position+1)
        elif current_position > 99:
            current_position = current_position - 100

        if current_position == 0:
            sol += 1
        print(current_position)

print(sol)
