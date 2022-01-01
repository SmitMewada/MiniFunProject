from graphics import line, showTable

def deleteOne(ID):
    person = findOne(ID)
    if not person:
        print("Data can't be deleted! 404.")
    else:
        with open("./files/txt1.txt", "r") as file:
            file_content = file.readlines()

        headers = file_content[:1]

        contents = [content.split(",") for content in file_content[1:]]

        if person in contents:
            contents.remove(person)
            new_list = ""

            for content in contents:
                new_list += ",".join(content)

            with open("./files/txt1.txt", "w") as file:
                file.write(headers[0] + new_list)

            print("Row deletion SUCCESSFUL!")
        else:
            print("Error occured with system!")
        

def findOne(ID):
    person = []
    with open("./files/txt1.txt", "r") as file:
        file_content = file.readlines()
    contents = file_content[1:]
    flag = False

    for content in contents:
       
        if int(content.split(",")[0]) == ID:
            person = content
            flag = True
            break

    print("Not found!") if not flag else print(person)
    return person.split(",") if person else None
    
        
def getData():
    with open("./files/txt1.txt", "r") as file:
        file_content = file.readline()
    header = [ header for header in file_content.split(",")]
    showTable(header)
    line(header)

    with open("./files/txt1.txt", "r") as file:
        file_content = file.readlines()
    contents = file_content[1:]
    
    for content in contents:
        for value in content.split(","):
          print(value, end=" ")

def getLastID():
    with open("./files/txt1.txt", "r") as file:
        content = file.readlines()
    return int(content[-1].split(",")[0])

def insertData():
    name = input("Enter your name: ")
    surname = input('Enter your surname: ')

    with open("./files/txt1.txt", "a") as file:
        file.write(f"\n{getLastID()+1},{name},{surname}")

    print("Data entered SUCCESSFULLY!")
    return True
