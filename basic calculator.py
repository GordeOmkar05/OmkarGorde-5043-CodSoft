


def calculator():
    print("\n---------------WELCOME TO SIMPLE CALCULATOR---------------\n")
    
 
    
    while True:
        num1=float(input("Enter the input of first element: "))
        
        num2=float(input("Enter the input of second element: "))
        
        print("Please enter operation to be done:")
        print(int("1.Addition\n2.Substraction\n3.Multiplication\n4.Division\n5.Mod Division\n"))
        opr=input()
        match opr:
             case "1":
                 result= num1 + num2
                 print(f"Result of Addition of {num1} + {num2} is:{result}")
           
             case "2":
                  result= num1 - num2
                  print(f"Result of Substraction of {num1} - {num2} is:{result}")
             case "3":
                  result= num1 * num2
                  print(f"Result of Multiplication of {num1} * {num2} is:{result}")
             case "4":
                  result= num1 / num2
                  print(f"Result of Division of {num1} / {num2} is:{result}")
             case "5":
                  result= num1 % num2
                  print(f"Result of Mod Division of {num1} * {num2} is:{result}")
             case _:
                  print("Please give valid inputs!!")
                  return
        
                  
        user_response=input("Do you want to continue (yes/no):")
        if(user_response!="yes"):
             break


if(__name__=="__main__"):
     calculator()
