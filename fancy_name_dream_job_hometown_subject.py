# Pseudocode

# 1. Import necessary libraries for fancy printing
import art
from colorama import Fore, Style

# 2. Print a welcome message explaining the purpose of the program
print(Fore.CYAN)
art.tprint("Welcome to my Program", font="small")
print(Style.RESET_ALL)
print("- This program display your name, dream job, hometown, and your favorite subject in a fancy way.")

# 3. Prompt the user to input their name
name = input("\nPlease enter your name: ")

# 4. Prompt the user to input their dream job
dream_job = input("Please enter your dream job: ")

# 5. Prompt the user to input their hometown
hometown = input("Please enter your hometown: ")

# 6. Prompt the user to input their favorite subject
favorite_subject = input("Please enter your favorite subject: ")

# 7. Print the user's name in a fancy
print("\nYour name in a fancy way: ")
print(Fore.BLUE, end="")
art.tprint(name, font="doh")
print(Style.RESET_ALL)

# 8. Print the user's dream job in a fancy way
print("\nYour dream job in a fancy way: ")
print(Fore.RED, end="")
art.tprint(dream_job, font="mscript")
print(Style.RESET_ALL)

# 9. Print the user's hometown in a fancy way
# 10. Print the user's favorite subject in a fancy way
# 11. Thank the user for using the program