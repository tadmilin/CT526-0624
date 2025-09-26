from mylib import myfunc
try:
    turns = int(input("How many turns you want to run?"))
    
    for i in range(1, turns + 1):
        result = myfunc("x", i)
        print(result)
        
except ValueError:
    print("enter number")
