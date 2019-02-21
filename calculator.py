import math as m 

def storage(number_1,operation,number_2):
     number_1=number_1
     operation=operate
     number_2=number_2
     if operation=='+':
         part_1=number_1+number_2
         return part_1
     elif operation=='-':
         part_1=number_1-number_2
         return part_1
     elif operation=='*':
         part_1=number_1*number_2
         return part_1
     elif operation=='/':
         part_1=number_1/number_2
         return part_1


def sqrt_make(number_1):
    part_1=m.sqrt(number_1)
    return part_1

   
    
available_operations=('+','-','*','/',)
print (available_operations)
choice_1=input('do you want to start with a square root number? ')


if choice_1=='y' or choice_1=='yes':
    num_1=float(input('enter the number 1: '))
    part_1=sqrt_make(num_1)
    print(part_1)

    while True:
        more_operations=input('do you want to perform more operations? ')
        if more_operations=='y' or more_operations=='yes':
            operate=input('Enter the operation you want to perform: ')
            choice_2=input('is your second number a square root? ')
            if choice_2=='y' or choice_2=='yes':
                num_2=float(input('Enter number 2: '))
                part_3=sqrt_make(num_2)
                part_1=storage(part_1,operate,part_3)
                print (part_1)
            else:
                num_2=float(input('enter number 2: '))
                part_1=storage(part_1,operate,num_2)
                print(part_1)
        else: 
            print('Final result',part_1)
            break       
else:
    num_1=float(input('enter the number 1: '))
    operate=input('Enter the operation you want to perform: ')
    choice_2=input('is your second number a square root? ')

    if choice_2=='y' or choice_2=='yes':
        num_2=float(input('Enter number 2: '))
        part_3=sqrt_make(num_2)
        part_1=storage(num_1,operate,part_3)
        print (part_1)
    else:
        num_2=float(input('enter number 2: '))
        part_1=storage(num_1,operate,num_2)
        print(part_1)

    while True:
        more_operations=input('do you want to perform more operations? ')
        if more_operations=='y' or more_operations=='yes':
            operate=input('Enter the operation you want to perform: ')
            choice_2=input('is your second number a square root? ')
            if choice_2=='y' or choice_2=='yes':
                num_2=float(input('Enter number 2: '))
                part_3=sqrt_make(num_2)
                part_1=storage(part_1,operate,part_3)
                print(part_1)
            else:
                num_2=float(input('enter the number: '))
                part_1=storage(part_1,operate,num_2)
                print(part_1)
        else: 
            print('Final result',part_1)
            break
        
        




