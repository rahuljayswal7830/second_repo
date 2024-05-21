# def recur(number):
#     if number==0:
#         print("End recursion")
#         return 1
#     else:
#         return number*recur(number-1)


def recur(number):
    first=0
    second=1
    if(number==0):
        print("End recuresion")
    else:
        pass
    

num=int(input("Enter number:= "))
mul=recur(num)
print(f"factorial := {mul}")