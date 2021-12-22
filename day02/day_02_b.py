with open("input.txt") as file:
    data = file.readlines()

aim, x, y = 0, 0, 0

for line in data:
    line = line.split()
    direction = line[0]
    ammount = int(line[1])

    if(direction == 'forward'):
        x+=ammount
        y+= (aim * ammount)
    elif(direction == 'down'):
        aim+=ammount
    else:
        aim-=ammount

final = x*y

print(final)