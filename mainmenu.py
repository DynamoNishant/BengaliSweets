from sys import exit
from time import sleep
import os

import product
import bill
import peoplesave


def procs(): # 2 second processing prompt and clearscreen
    print("PROCESSING INPUT...")
    sleep(2)
    os.system('cls')

def main():
    os.system('cls')
    print("\t\t\t\t\t\t\t BENGALI SWEETS CORNER\n\n\n")
    print("Main Menu")
    print("\n\n\t 1. Customer\n\t 2. Employee\n\t 3. Product\n\t 4. Bill\n\t 5. Exit ")

    choice = input(">> ")


    if choice == "1":
        procs()
        peoplesave.peepsmenu("CUSTOMER")

    elif choice == "2":
        procs()
        employee.emp_menu()

    elif choice == "3":
        procs()
        product.prod_menu()

    elif choice == "4":
        procs()
        bill.bill_menu()

    elif choice == "5":
        print("Closing .....")
        sleep(2)
        exit(0)

    else:
        procs()
        print("Type something meaninful")
        sleep(1)
        os.system('cls')

        main()




if __name__ == "__main__":
    main()
