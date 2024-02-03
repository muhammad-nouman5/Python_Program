l=[]
while True:
    c=int(input('''
    1 Push Elements
    2 Pop First Elements
    3 Front Elements
    4 Last Elements
    5 Display List
    6 Exit
    '''))
    if c==1:
        n=input("Enter Value for Stack List:- ")
        l.append(n)
        print(l)
    elif c==2:
        if len(l)==0:
            print("Empty Stack")
        else:
            del l[0]
            print(l)
    elif c==3:
        if len(l)==0:
            print("Empty Stack")
        else:
            print("First Stack Element:- ",l[0])
    elif c==4:
        if len(l)==0:
            print("Empty Stack")
        else:
            print("Last Stack Element:- ",l[-1])
    elif c==5:
        print("Display Stack List:- ",l)
    elif c==6:
        break