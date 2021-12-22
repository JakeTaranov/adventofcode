with open("input.txt") as file:
    data = [int(i) for i in file.read().strip().split("\n")]

n = len(data)
count = 0

for i in range(1, n):
    if(data[i] > data[i-1]):
        count += 1

print(count)