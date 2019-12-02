codes = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,19,5,23,2,9,23,27,1,5,27,31,1,5,31,35,1,35,13,39,1,39,9,43,1,5,43,47,1,47,6,51,1,51,13,55,1,55,9,59,1,59,13,63,2,63,13,67,1,67,10,71,1,71,6,75,2,10,75,79,2,10,79,83,1,5,83,87,2,6,87,91,1,91,6,95,1,95,13,99,2,99,13,103,1,103,9,107,1,10,107,111,2,111,13,115,1,10,115,119,1,10,119,123,2,13,123,127,2,6,127,131,1,13,131,135,1,135,2,139,1,139,6,0,99,2,0,14,0]

index = 0
check_num = 3
while True:
    for num in codes:
        check_num += 1
        if check_num == 4:
            check_num = 0
            if num in (1, 2, 99):
                if num == 1:
                    position1 = codes[index + 1]
                    position2 = codes[index + 2]
                    output_position = codes[index + 3]
                    codes[output_position] = codes[position1] + codes[position2]
                elif num == 2:
                    position1 = codes[index + 1]
                    position2 = codes[index + 2]
                    output_position = codes[index + 3]
                    codes[output_position] = codes[position1] * codes[position2]
                else:
                    print("HERE!")
                    break

        index += 1
    break

print(codes[0])
print(codes[1])
print(codes[2])
print(codes)
