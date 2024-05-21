class Practice:
    def __init__(self):
        pass


    #*********for question 1 to add two numbers
    @staticmethod   
    def add():
        num1=float(input("Enter First number: "))
        num2=float(input("Enter Second number: "))
        print("Sum of Two numbers = ",num1+num2)
    
     #*********for question 2 to average three numbers
    @staticmethod   
    def avg():
        num1=float(input("Enter First number: "))
        num2=float(input("Enter Second number: "))
        num3=float(input("Enter Third number: "))
        avg=(num1+num2+num3)/3
        print("Average of three numbers = ",avg)

    #*********for question 3 to simple intreset
    @staticmethod   
    def simple_ins():
        p=float(input("Enter principle amount: "))
        r=float(input("Enter rate of interest : "))
        t=float(input("Enter time in year: "))
        si=(p*r*t)/100
        print("Simple interest = ",si)


    #*********for question 4 to converting temp from celsius to fohrenheit
    @staticmethod
    def convert_temp():
        temp=float(input("Enter tempreture in celsius: = "))
        temp_F=(temp*9/5)+32
        print("temp in fohrenheit := ",temp_F)

    #*********for question 5 to number positive or not
    @staticmethod
    def check_number():
        num1= float(input("Enter number:= "))
        if(num1>0):
            print("Number is positive")
        else:
            print("Number is negative")

    #*********for question 6 to leap year
    @staticmethod
    def check_leap_year():
        num1= int(input("Enter Year:= "))
        if(num1%400==0):
            print("Year is leap year")   
        elif(num1%100==0):
            print("Year is not leap year")
        elif(num1%4==0):
            print("Year is leap year")
        else:
            print("Year is not leap year")

    #*********for question 9 to sum of paticular range number
    @staticmethod 
    def sum():
        start=int(input("enter start your range:= "))
        end=int(input("enter start your range:= "))
        sum_of_number=0
        for i in range(start,end+1):
            sum_of_number+=i
        print("totla sum: = ",sum_of_number)

    #*********for question 10 to table
    @staticmethod
    def table():
        num=int(input("Enter number := "))
        for i in range(1,11):
            print(f"{num} X {i} = {num*i}")

    #*********for question 11 to check prime number 
    @staticmethod
    def check_prime():
        num=int(input("Enter number := "))
        if(num==2):
            print("number is prime")
        elif(num==1 or num==0):
            print("please enter number grater than 2")
        else:
            for i in range(2,11):
                if i<num and num%i==0:
                    print("number is not prime")
                    break
            else:
                print("number is prime")

    #*********for question 12 to factorial
    @staticmethod
    def fact():
        num=int(input("Enter number := "))
        mul=1
        for i in range(num,0,-1):
            mul*=i
        print(f"factorial of number := {mul}")

    #**** question 13 and question 16 too count number digit and reverse number also
    @staticmethod
    def digit_count():
        num=int(input("Enter number := "))
        count=0
        reverse_num=0
        
        while num>0:
            diviation=num//10
            remainder=num%10
            num=diviation
            reverse_num=reverse_num*10+remainder
            count+=1
        print(f"reverse number:= {reverse_num}")
        print(f"count number:= {count}")
 

    #********question 14 sum of all digit
    @staticmethod
    def sum_digit():
        num=int(input("Enter your number:= "))
        sum=0
        while num>0:
            divide=num//10
            remainder=num%10
            sum+=remainder
            num=divide
        print(f"sum of number := {sum}")

    #******question 17 for palindrome
    @staticmethod
    def palindrome():
        num=int(input("Enter your number:= "))
        reverse_num=0
        temp=num
        while num>0:
            divide=num//10
            remainder=num%10
            num=divide
            reverse_num=reverse_num*10+remainder
        if(reverse_num==temp):
            print("number is armstrong")
        else:
            print("number is not armstrong")
    
    #*********** question 15 for armstorng
    @staticmethod
    def armstrong():
        num=int(input("Enter your number:= "))
        temp=num
        number_cube=0
        while num>0:
            divide=num//10
            remainder=num%10
            num=divide
            number_cube+=remainder**3
        if(number_cube==temp):
            print("number is armstrong")
        else:
            print("number is not armstrong")

    #* question 18 all prime number from 1 to given number
    @staticmethod
    def all_prime():
        num = int(input("Enter your number: "))
        if(num==0 or num ==1 ):
            print("enter number is greater than 2")
        elif (num==2):
            print(f"prime number is {num}")
        else:
            for i in range(2,num+1):
                for divider in range(2,11):
                    if(i>divider and i%divider==0):
                        break
                else:
                    print(f"prime number is : {i}")

    #********* question 24 with third variable
    @staticmethod
    def swap():
        num1=int(input("Enter first number:= "))
        num2=int(input("Enter second number"))
        temp=num1
        num1=num2
        num2=temp
        print(f"First Number:= {num1}")
        print(f"Second Number: = {num2}")

    #*********question 25 swapping without third variable
    @staticmethod
    def swap_without_temp():
        num1=int(input("Enter first number:= "))
        num2=int(input("Enter second number:= "))
        num1=num1+num2
        num2=num1-num2
        num1=num1-num2
        print(f"First Number:= {num1}")
        print(f"Second Number: = {num2}")




            





    


obj=Practice()
# obj.add()
# obj.avg()
# obj.simple_ins()
# obj.convert_temp()
# obj.check_number()
# obj.check_leap_year()
# obj.sum()

# obj.check_prime()
# obj.fact()
# obj.digit_count()
# obj.sum_digit()
# obj.palindrome()
# obj.armstrong()
# obj.all_prime()
# obj.swap()
obj.swap_without_temp()