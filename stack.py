l=[]
while True:
    c=int(input('''
    1 Push Elements
    2 Pop Elements
    3 Peek Elements
    4 Display List
    5 Exit
    '''))
    if c==1:
        n=input("Enter Value for Stack List:- ")
        l.append(n)
        print(l)
    elif c==2:
        if len(l)==0:
            print("Empty Stack")
        else:
            p=l.pop()
            print(p)
            print(l)
    elif c==3:
        if len(l)==0:
            print("Empty Stack")
        else:
            print("Last Stack Element:- ",l[-1])
    elif c==4:
        print("Display Stack List:- ",l)
    elif c==5:
        break