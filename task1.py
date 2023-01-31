# pylint: disable=missing-module-docstring
import random
x = random.randint(1000, 9999)
NUM = 0
while NUM < 1000 or NUM > 9999:
    NUM = int(input("Please enter a 4 digit number: "))
    if NUM < 1000 or NUM > 9999:
        print("invalid input")

print("system generated number is ", x)
print("The number you entered is ", NUM)
if NUM == x:
    print("Congrats you win")
else:
    RABBIT = 0
    TORTOISE = 0
    UNUM = str(NUM)
    SNUM = str(x)
    C1 = 0
    for i in UNUM:
        C1 = C1+1
        C2 = 0
        for j in SNUM:
            C2 = C2+1
            if i == j:
                if C1 == C2:
                    RABBIT = 1
                else:
                    TORTOISE = 1
    if RABBIT == 1:
        print("you got rabbit")
    elif RABBIT == 0 and TORTOISE == 1:
        print("you got tortoise")
    else:
        print("Bad Luck you don't have any match")
