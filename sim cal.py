#Create a simple calculator
print('''
      1 Add
      2 subract
      '''
      )
      
num1=int(input("Enter the value 1: "))
num2=int(input("Enter the value 2: "))
opr=input("Enter the opr ")
if opr=="1":
    print(num1+num2)
elif opr=="2":
    print(num1-num2)
else:
    print("invalid")
    
 
