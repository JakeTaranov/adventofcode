import string

with open("inputt.txt") as file:
    data = file.readlines()

n = len(data[0])
one_count, zero_count = 0, 0
original_bits = ""

for i in range(n):
    if(one_count > zero_count):
        original_bits += '1'
    elif(zero_count > one_count):
        original_bits += '0'

    one_count, zero_count = 0, 0
    for j in range(len(data)):
        if(data[j][i] == "1"):
            one_count += 1
        else:
            zero_count += 1

#Inverting Bits
inverted_bits = original_bits.translate(str.maketrans("10", "01"))

decimal_bits = int(original_bits, 2)
decimal_inverted_bits = int(inverted_bits, 2)

print(decimal_bits * decimal_inverted_bits)

