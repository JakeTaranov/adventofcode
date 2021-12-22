with open("input.txt") as file:
    data = file.readlines()

x, y = 0, 0

for line in data:
    line = line.split()
    direction = line[0]
    ammount = int(line[1])

    if(direction == 'forward'):
        x+=ammount
    elif(direction == 'down'):
        y+=ammount
    else:
        y-=ammount

final = x*y

print(final)
