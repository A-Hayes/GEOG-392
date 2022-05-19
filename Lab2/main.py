# Asa Hayes
# GEOG-3923
# Lab 2: For Loops

part1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
sum1 = 0

for i in part1:
    sum1 = sum1 + i
    
print("Sum of List part1: ", sum1)

part2 = [-1, 23, 483, 8573, -13847, -381569, 1652337, 718522177]
sum2 = 0

for i in part2:
    sum2 = sum2 + i
    
print("Sum of List part2: ", sum2)

part3 = [146, 875, 911, 83, 81, 439, 44, 5, 46, 76, 61, 68, 1, 14, 38, 26, 21] 
sum3 = 0

for i in part3:
    if i % 2 == 0:
        sum3 = sum3 + i
    
print("Sum of List part3: ", sum3)