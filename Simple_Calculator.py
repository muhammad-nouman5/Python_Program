print('''
+ Addition
- Subtraction
* Multiplication
/ Divide
''')
num1=int(input("Enter Num1 :- "))
num2=int(input("Enter Num2 :- "))
opr=input("Enter Operator +,*,-,/ :- ")
if opr=="+":
    add=num1+num2
    print("Addition of Num1 and Num2 :- ",add)
elif opr=="-":
    sub=num1-num2
    print("Subtraction of Num1 and Num2 :- ",sub)
elif opr=="*":
    mul=num1*num2
    print("Multiplication of Num1 and Num2 :- ",mul)
elif opr=="/":
    division=num1/num2
    print("Division of Num1 and Num2 :- ",division)
else:
    print("You Enter Wrong Values")