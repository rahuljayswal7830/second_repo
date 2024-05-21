

#************question 7 for calculator
class Menu:
    options="y"
    def __init__(self):
        print("*******************************")
        print("Choose Options: ")
        print("1 For addtion")
        print("2 For subtraction")
        print("3 For multiplication")
        print("4 For dividation")
        self.ans= int(input("Enter Your options:= "))
        

    def menu_func(self):
        if(self.ans==1):
            num1= float(input("Enter Frist Number:= "))
            num2= float(input("Enter second number:= "))
            obj=Calculator(num1,num2)
            res=obj.add()
            return res 
        elif(self.ans==2):
            num1= float(input("Enter Frist Number:= "))
            num2= float(input("Enter second number:= "))
            obj=Calculator(num1,num2)
            res=obj.sub()
            return res
        elif(self.ans==3):
            num1= float(input("Enter Frist Number:= "))
            num2= float(input("Enter second number:= "))
            obj=Calculator(num1,num2)
            res= obj.mul()
            return res
        elif(self.ans==4):
            num1= float(input("Enter Frist Number:= "))
            num2= float(input("Enter second number:= "))
            obj=Calculator(num1,num2)
            res= obj.divide()
            return res
        else:
            print("Please choose right number")
            return "y"



class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    
    def add(self):
        print("Sum of numbers:= ",self.num1+self.num2)
        ins=input("DO you want continue y/n:= ")
        if ins=="y":
            return "y"
    def sub(self):
        print("Subract of numbers:= ",self.num1-self.num2)
        ins=input("DO you want continue y/n:= ")
        if ins=="y":
            return "y"

    def mul(self):
        print("Multiplication of numbers:= ",self.num1*self.num2)
        ins=input("DO you want continue y/n:= ")
        if ins=="y":
            return "y"
    
    def divide(self):
        if(self.num2!=0):
            print("dividation of numbers:= ",self.num1/self.num2)
        else:
            print("Numbers are not divisable")
        ins=input("DO you want continue y/n:= ")
        if ins=="y":
            return "y"
        
options="y"
while options=="y":
    menu_obj=Menu()
    options=menu_obj.menu_func()



