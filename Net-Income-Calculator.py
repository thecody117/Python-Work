import os
import ctypes
from pathlib import Path
#Sets the CMD window title
ctypes.windll.kernel32.SetConsoleTitleW("New York Net Pay Calculator")
#Clears the command window, use clear() to do it at any time.
clear = lambda: os.system('cls')
clear()
print("Welcome to the New York Net Pay Calculator.")
while True:
    try:
        Hours = float(input("How many hours did you work?: "))
        if Hours < 0:
            raise ValueError()
        break
    except ValueError:
        print("Please enter something valid, such as a positive number.")
while True:
    try:
        HourlyPay = float(input("What is your hourly pay?: "))
        if HourlyPay < 0:
            raise ValueError()
        break
    except ValueError:
        print("Please enter something valid, such as a positive number.")
OvertimePay = float(HourlyPay) * 1.5
while True:
    try:
        Tax = float(input("What is the tax rate that is going to be used?: "))
        if Tax < 0:
            raise ValueError()
        break
    except ValueError:
        print("Please enter something valid, such as a positive number.")
if float(Hours) > 40:
    OvertimeHours = float(Hours) - 40
    Hours = 40
    FrstGrsPart = int(Hours) * float(HourlyPay)
    ScndGrsPart = float(OvertimeHours) * float(OvertimePay)
    GrossPay = float(FrstGrsPart) + float(ScndGrsPart)
    print("Calculating Gross Pay...")
    print("Your Gross Pay is " + "$" + str(GrossPay))
    print("Calculating Net Pay")
    GrossPayTax = float(GrossPay) * float(Tax)
    NetPay = float(GrossPay) - float(GrossPayTax)
    print("Your Net Pay is " + "$" +str(NetPay))
elif float(Hours) < 40:
    GrossPay = float(Hours) * float(HourlyPay)
    print('Calculating Gross Pay...')
    print('Your Gross Pay is ' + "$" + str(GrossPay))
    print("Calculating Net Pay...")
    GrossPayTax = float(GrossPay) * float(Tax)
    NetPay = float(GrossPay) - float(GrossPayTax)
    print("Your Net Pay is " + "$" +str(NetPay))
input("Calculations complete, please write these down or just remember them. \n Awaiting input...")
