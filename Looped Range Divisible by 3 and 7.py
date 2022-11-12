#===============================================================================
#Program Name: Looped Numbers Divisible by 3 and 7
# Your Name: Keegan Bramlet
# Date: Novemeber 6, 2022
# Program Purpose: Display numbers from 1-50, indicating which values are divisible by 3 and 7
#===============================================================================
n=51
for i in range(1, n):
    if (i % 3) == 0 and (i % 7) != 0: 
        print("Divisible by 3")
    if (i % 7) == 0 and (i % 3) != 0:
        print("Divisible by 7")
    if (i % 3) == 0 and (i % 7) == 0:
        print("Divisible by Both")
    if (i % 3) != 0 and (i % 7) != 0:
        print(i)

for i in range(1, 51):
#check both divisible cases, then divisible by 3 case, divisible by 7 case
    if i%3 == 0 and i % 7 == 0:
        print("Divisible by Both")
    elif i % 3== 0:
        print("Divisible by 3")
    elif i % 7 == 0:
        print("Divisible by 7")
    else:  #none of cases, print a number
        print(i)
