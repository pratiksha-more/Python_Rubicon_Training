def calculator():
    print("1.Addition ")
    print("2.Subtraction ")
    print("3.Multiplication ")
    print("4.Division")


    ch=int(input("Enter The Choice : "))

    if ch in [1,2,3,4]:
        num1=int(input("Enter The Num1 : "))
        num2=int(input("Enter The Num2 : "))

        if ch==1:
            result=num1+num2
            print("Addition  : ",result)
            
        elif ch==2:
            result=num1-num2
            print("Subtraction : ",result)

        elif ch==3:
            result=num1*num2
            print("Multiplication :",result)

        elif ch==4:
            if num2!=0:
                result=num1/num2
                print("Division :",result)
            else:
                print("Error! Division by zero.")

        else:
            print("Invalid")

calculator()
            
            
