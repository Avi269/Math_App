import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def fact(x):
    f=1
    for i in range(1,x+1):
        f*=i
    return f
    
def perm(n,r):
    return fact(n)/fact(n-r)

def comb(n,r):
    return fact(n)/(fact(n-r)*fact(r))
    
while True:
    clear_screen()
    print("Choose an option from the list:\n\t1. Factorial\n\t2. Permtation\n\t3. Combination\n\t0. Exit\n")

    a=int(input("Enter your choice here (only option number): "))

    if a==1:
        result=fact(int(input("\nEnter number: ")))
        print("\nAnswer: ", result)
    elif a==2:
        result=perm(int(input("\nEnter 'n': ")), int(input("Enter 'r': ")))
        print("\nAnswer: ", result)
    elif a==3:
        result=comb(int(input("\nEnter 'n': ")), int(input("Enter 'r': ")))
        print("\nAnswer: ", result)
    elif a==0:
        print("\nExiting the program...")
        break
    else:
        print("\nInvalid input!")
    
    input("\n\nPress enter to continue...")
