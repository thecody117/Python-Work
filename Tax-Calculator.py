import os
import ctypes
from pathlib import Path
#Sets the CMD window title
ctypes.windll.kernel32.SetConsoleTitleW("New York State Tax Calculator")
#Clears the command window, use clear() to do it at any time.
clear = lambda: os.system('cls')
clear()
print("Welcome to the Upstate New York Tax Calculator.")
#checks if the file Tax-Calculator-Tax exists
my_file = Path("Tax-Calculator-Tax.txt")
#if it does exist
Start = True
Continue = True
while Start == True:
    if my_file.is_file():
        Start = False
        File = open("Tax-Calculator-Tax.txt", "r+")
        #used to tell the number currently in the file.
        fileTax = File.read()
        print("the tax currently on file is: " + fileTax + "%")
        givenAnswer = input("Is this still true?: ")
        givenAnswer.lower()
        if givenAnswer == "y":
            givenAnswer = "yes"
        if givenAnswer == "yes":
            #keeps program running once this starts.
            while Continue == True:
                Cost = input("How much did the item cost?: ")
                #converts to both an int and a float.
                CostAfterTax = int(Cost) * float(fileTax)
                TotalCost = CostAfterTax + int(Cost)
                File.close()
                print("The Cost after tax is: " + "$" + str(TotalCost))
                Quit = input("Would you like to do another calculation?: ")
                Quit.lower()
                if Quit == "y":
                    Quit = "yes"
                if Quit == "yes":
                    print("Alright.")
                else:
                    Continue = False
        else:
            TaxUpdate = input("Please input new tax amount: ")
            #closes the file from Read, then opens it again in write
            #which deletes the content of the file before writing to it.
            File.close()
            File = open("Tax-Calculator-Tax.txt", "w")
            File.write(TaxUpdate)
            File.close()
        #and when it does not, Should only run when first started up.
    else:
        #creates the file when it does not exist.
        #Need to make this code loop back to the start, then stop the loop.
        print("File does not exist, creating file. Please restart program after this is completed. \n")
        File = open("Tax-Calculator-Tax.txt", "w")
        print("Make sure to set the tax rate as a decimal, whole numbers fuck it up. \n")
        NewTax = input("What is the current tax rate?: ")
        File.write(NewTax)
        File.close()
