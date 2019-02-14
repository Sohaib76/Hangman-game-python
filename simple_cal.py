print('                             SIMPLE CALCULATOR with PYTHON                       ')
print()
print()
print()

while True:
    print()
    print()
    operation = input('what operation you want to perform? (+ - * / Quadratic_Equation(eq) ): ')
    print()


    add_l = []

    def add ():
        try:
            while True:
                a = input('Enter a number: ')
                b = input('enter another number: ')

                if not a:
                    a = 0
                if not b:
                    b = 0
                d = float(a)
                e = float(b)    

                c= d+e

                add_l.append(c)

                another = input('do you want to enter another number? (y/n): ').lower()

                if another == 'y':
                    continue
                
                else:
                    print('Result: ', sum(add_l))
                    break
        except Exception as abc:
            print('something went wrong!', abc)



    sub_l = []

    def subtract():
        try:
            total_numbers = int(input('how many number do you want to subtract? :  '))
            print()
            print('Please enter the number from which you want to subtract other numbers at first.')

            t_count = 0

            while t_count < total_numbers:
                a= input('enter a number: ')
                if not a:
                    a= 0
                b= float(a)

                
                sub_l.append(b)
                
                t_count = t_count +1


                subtract_list = sum(sub_l, -sub_l[0])


            answer = sub_l[0] - subtract_list
            print('Result: ', answer)
        except Exception as abc:
            print('something went wrong!', abc)

    mul_l= []

    def multiply():
        while True:
            try:
                a = input('enter a number: ')
                b = input('enter another number: ')

                if not a:
                    a = 0
                if not b:
                    b = 1

                d = float(a)
                e = float(b)    
                c= d*e

                mul_l.append(c)

                another= input('do you want to multiply more numbers to this? (y/n): ').lower()
                
                if another== 'y':
                    continue
                else:
                    import functools
                    print('Result: ', functools.reduce(lambda a,b: a*b,mul_l))
                    break
            except Exception as abc:
                print('somthing went wrong!', abc)


    def divide():
        try:
            while True:
                Note= print('Note: Only two numbers can be divided once.')
                print()
                print()
                
                a1= input('Enter the dividend (Numerator): ')
                b1= input('Enter the divider (de-numerator): ')

                if bool(a1) == False:
                    a1 = 0
                if bool(b1) == False:
                    b1 = 1
                a= float(a1)
                b= float(b1)
                
                answer_float = a/b
                answer_int = a//b
                import fractions

                answer_fraction = fractions.Fraction(answer_float)
                
                print()
                print(f'Result (float value): {answer_float}')
                print(f'Result (integer value): {answer_int}')
                print(f'Result (fraction value): {answer_fraction}')

                print()
                print()

                another= input('do you want to perform another division?(y/n): ').lower()

                if another == 'y':
                    continue
                else:
                    break
        except Exception as abc:
            print('something went wrong!', abc)

    
    def quadratic_equation():
        try:
            print(f'Quadratic Equation Menu.. Please Enter the required values.')
            print()
            print()
            a1 = input('Please enter the value of a:  ')
            b1 = input('Please enter the value of b:  ')
            c1 = input('Please enter the value of c:  ')

            if not a1:
                a1 = 0
            if not b1:
                b1 = 0
            if not c1:
                c1 =0
            
            a= float(a1)
            b= float(b1)
            c= float(c1)

            import math

            x1= (-b+ math.sqrt(b**2 - 4*c)) / (2*a)
            x2= (-b- math.sqrt(b**2 - 4*c)) / (2*a)

            import fractions

            print()
            print()
            print()
            

            print(f'Result is: X1 = {x1}')
            print(f'           X2 = {x2}') 
            print()
            print(f'In fraction: X1 = {fractions.Fraction(x1)}')
            print(f'             X2 = {fractions.Fraction(x2)}')
        except Exception as abc:
            print('something went wrong!', abc)


    if operation == '+':
        add()

    elif operation == '-':
        subtract()

    elif operation == '*':
        multiply()

    elif operation == '/':
        divide()
    
    elif operation.lower() == 'eq':
        quadratic_equation()

    else:
        print('Invalid Entry!')

    print()
    again = input('Do you want to perform another calculation? (y/n)').lower()

    if again == 'y':
        continue
    else:
        print()
        print('I hope that it was helpful.')
        print()    
        input('press enter to exit...')
        break