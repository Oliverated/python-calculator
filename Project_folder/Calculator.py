def add(a, b):
    print(a + b)


def sub(a, b):
     print( "Your answer is: ",a - b)


def mal(a, b):
     print("Your answer is: ",a * b)


def div(a, b):
    if b != 0:
         print("Your answer is: ", a / b)
    else:
        print( "Your answer is: ",a)



def main():
    while True:
        calculate_opt1 = input("1(+)\n 2(-)\n 3(x)\n 4(/)\n Q/5(quit) \n Choose am operation: ")
        if calculate_opt1 == "1":
            add(float( input('enter a number: ')),float( input('enter a number: ')))
        elif calculate_opt1 == "2":
            sub(float( input('enter a number: ')),float( input('enter a number: ')))
        elif calculate_opt1 == "3":
            mal(float( input('enter a number: ')),float( input('enter a number: ')))
        elif calculate_opt1 == "4":
            div(float(input('Enter a number: ')), float(input('Enter a number: ')))
        elif calculate_opt1 == "5" or calculate_opt1 == "Q" or calculate_opt1 == 'q':
            print('Calculation ended!!')
            quit()
        else:
          print(f" '{calculate_opt1}' is not among my commands")




if  __name__=="__main__":
    main()