def showTable(header):
    for head in header:
        print(head, end=" , ")

def square():
    for i in range(0, 5):
        print("*", end=" ")
        for j in range(0, 10):
            if i==0 or i==4:
                print("*", end=" ")
            else:
                print(" ", end=" ")
            if j == 9:
                print("*")

def line(value):
    text = ""
    for i in value:
        text = text + i
    for i in range(0, len(text)):
        print("*", end="")
    print("\n")


           
            
            
        