
# This is Basic Calculator for CodSoft Internship

def calculator():
    print("\n---------------WELCOME TO SIMPLE CALCULATOR---------------\n")
    
 
    
    while True:
        num1=float(input("Enter the input of first element: "))
        if(num1=='.'):
             num1=float(num1)
        else:
             num1=int(num1)
        num2=float(input("Enter the input of second element: "))
        if(num2=='.'):
             num2=float(num2)
        else:
             num2=int(num2)
        print("Please enter operation to be done:")
        print("1.Addition\n2.Substraction\n3.Multiplication\n4.Division\n5.Mod Division\n")
        opr=input()
        match opr:
             case "1":
                 result= num1 + num2
           
             case "2":
                  result= num1 - num2
             case "3":
                  result= num1 * num2
             case "4":
                  result= num1 / num2
             case "5":
                  result= num1 % num2
             case _:
                  print("Please give valid inputs!!")
                  return
        if isinstance(result, float) and result.is_integer():
             result = int(result)
        print(f"Result: {result}")
                  
        user_response=input("Do you want to continue (yes/no):")
        if(user_response!="yes"):
             break


if(__name__=="__main__"):
     calculator()