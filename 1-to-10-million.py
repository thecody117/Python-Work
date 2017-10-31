print("This program will write a x = and then a number all the way from 1 to any number.")
print("\n This also writes a file that is up to 122MB or more in size.")
FinalNum = input("what do you want the final number to be? : ")
Answer = input("Are you sure you want to run this? : ")
Answer = Answer.lower()
if Answer == "y":
    x = 0
    file = open("1-to-10-Million.txt", "w")
    while x < int(FinalNum):
        print("x = ", x)
        x += 1
        file.write('x = ')
        file.write(str (x))
        file.write("\n")
    file.close()
    input("Press enter to continue...")
else:
    print("Good Choice")
    input("Press enter to continue...")
