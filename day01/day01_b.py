with open("input.txt") as file:
    data = [int(i) for i in file.read().strip().split("\n")]

n = len(data)

moving_sum = sum(data[:3])
prev_moving_sum = 1 << 60
count = 0


for i in range(n-3):
    if moving_sum > prev_moving_sum:
        count+=1

    moving_sum = prev_moving_sum

    moving_sum -= data[i]
    moving_sum += data[i+3]


if moving_sum > prev_moving_sum:
    count+=1

print(count)