#*****************question 8 for grade 

class Student:
    def __init__(self,name ,mark,mark2,mark3):
        self.name=name
        self.marks1=marks1
        self.marks2=marks2
        self.marks3=marks3

    
    def percentage(self):
        percentage_of_marks=((marks1+marks2+marks3)*100)/300
        self.percentage_of_marks=percentage_of_marks
        self.grade()
    
    def grade(self):
        if(self.percentage_of_marks>85):
            print(f"{self.name} has got grade A")
        elif(self.percentage_of_marks<85 and self.percentage_of_marks>=75):
            print(f"{self.name} has got grade B")
        elif(self.percentage_of_marks<75 and self.percentage_of_marks>=50):
            print(f"{self.name} has got grade C")
        elif(self.percentage_of_marks<50 and self.percentage_of_marks>=30):
            print(f"{self.name} has got grade D")
        else:
            print(f"{self.name} Failed")


name=input("Enter student name:= ")
marks1=int(input("Enter First subject marks:= "))
marks2=int(input("Enter Second subject marks:= "))
marks3=int(input("Enter Third subject marks:= "))
obj=Student(name,marks1,marks2,marks3)
obj.percentage()

