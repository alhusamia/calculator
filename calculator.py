def main():
	#write your code here
        number1 =input("Enter the first number: ")
        number2 =input("Enter the second number: ")
        operation = input("Choose the operation (+, -, /, *): ")
        if number1.isalpha():
            print("The number were invalid")
        else:
            if number2.isalpha():
                print("The number were inalid")
            else:
                if operation == "+":
                    x=int(number1)+int(number2)
                    print("The answer is "+str(x))
                elif operation == "-":
                    y = int(number1)-int(number2)
                    print("The answer is "+str(y))
                elif operation == "/":
                    z =int(number1)/int(number2)
                    print("The answer is "+str(z))
                elif operation == "*":
                    v=int(number1)*int(number2)
                    print("The answer is "+str(v))
                else:
                    print("The operation is not valid ")


        



if __name__ == '__main__':
	main()
