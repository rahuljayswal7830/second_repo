from array import array

#*******question-1 getting missing number
def missing_number(sequence):
    count=1
    for i in sequence:
        if(count==i):
            count+=1
        else:
            print(f"missing number=: {count}")
            break
        

missing_number([1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20])


#********question- 2 and 5 dublicates numbers changes add 

def dupicate(squence):
    dupicate_numbbers=[]
    unique_value=set()
    for i in squence:
        if i not in unique_value:
            unique_value.add(i)
        else:
            dupicate_numbbers.append(i)
    print(f"Dublicates numbers := {dupicate_numbbers}")
dupicate([1,2,3,2,4,1,5])


#******question- 3  getting maxium and minimum number
def largest_smallest(sequence):
    max_number=sequence[0]
    min_number=sequence[0]
    for i in sequence:
        if i>max_number:
            max_number=i
        if i< min_number:
            min_number=i
    
    print(f"max number is = {max_number}")
    print(f"min number is = {min_number}")

largest_smallest([23,21,11,34,56,78,12,8,])


#********question 6 removing duplicates 
def remove_duplicates(sequence):
    unique_values=[]
    for idx,i in enumerate(sequence):
        if i not in unique_values:
            unique_values.append(i)
    print(f"After removing duplicates = {unique_values}")
remove_duplicates([1,4,5,1,2,6,7,2,3])

#question 


            
