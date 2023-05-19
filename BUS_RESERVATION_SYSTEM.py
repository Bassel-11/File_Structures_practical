def writeToFile():
    try:
        with open("passengers.txt", "a") as file:
            c = 'y'
            while c == 'y':
                id=input("enter your ID : ")
                name=input("enter your Name : ")
                age=input("enter your Age : ")
                destination=input("enter your Destination : ")
                file.write(id + '\t' + name + '\t' + age + '\t' + destination + '\n')
                c = input("Do you want to enter a new record ( y / n) ? ")
            print("record added successfully")
    except Exception as e:
        print("Error occurred while writing to file:", e)

def readFromFile():
    try:
        print("ID\tName\tAge\tDestination")
        print("----------------------------")
        with open("passengers.txt", "r") as file:
            for line in file:
                print(line,end="")
    except Exception as e:
        print("Error occurred while reading from file:", e)

def SearchById():
    try:
        id = input("enter Id to search : ")
        flag = False
        with open("passengers.txt", "r") as file:
            for line in file:
                l  = line.split('\t')
                if l[0]==id:
                    flag=True
                    print("ID\tName\tAge\tDestination")
                    print("----------------------------")
                    print(line)
                    return
        if not flag:
            print("record not found")
    except Exception as e:
        print("Error occurred while searching for record:", e)

def deleteRecord():
    try:
        import os
        id = input("enter Id to delete : ")
        file = open("passengers.txt", "r")
        tempfile = open("tmp.txt", "w")
        flag = False
        for line in file:
            l=line.split('\t')
            if id==l[0]:
                flag = True
            else:
                tempfile.write(line)
        file.close()
        tempfile.close()
        os.remove("passengers.txt")
        os.rename("tmp.txt", "passengers.txt")
        if not flag:
            print("record does not exist")
        else:
            print("the record deleted successfully")
    except Exception as e:
        print("Error occurred while deleting record:", e)

def updateRecord():
    try:
        import os
        id = input("enter Id you want to update : ")
        field = input("Which field do you want to update \n1 - ID\n2 - Name\n3 - Age\n4 - Destination\nYour choice :  ")
        file = open("passengers.txt", "r")
        tempfile = open("tmp.txt", "w")
        flag = False
        for line in file:
            l = line.split('\t')
            if id != l[0]:
                tempfile.write(line)
            else:
                flag = True
                if field == "1":
                    new_id = input("enter new ID : ")
                    tempfile.write(new_id + '\t' + l[1] + '\t' + l[2] + '\t' + l[3])
                elif field == "2":
                    new_name = input("enter new Name : ")
                    tempfile.write(l[0] + '\t' + new_name + '\t' + l[2] + '\t' + l[3])
                elif field == "3":
                    new_age = input("enter new Age : ")
                    tempfile.write(l[0] + '\t' + l[1] + '\t' + new_age + '\t' + l[3])
                elif field == "4":
                    new_dest = input("enter new Destination : ")
                    tempfile.write(l[0] + '\t' + l[1] + '\t' + l[2] + '\t' + new_dest)
        file.close()
        tempfile.close()
        os.remove("passengers.txt")
        os.rename("tmp.txt", "passengers.txt")
        if not flag:
            print("record does not exist")
        else:
            print("record updated successfully")
    except Exception as e:
        print("Error occurred while updating record:", e)

def main():
    while True:
        try:
            print("\n------------BUS RESERVATION SYSTEM---------------")
            print("(Choose one of these to do)")
            print("1 - Enter new passenger")
            print("2 - View all passengers")
            print("3 - Search for a passenger")
            print("4 - Change passenger information")
            print("5 - Delete a passenger")
            print("6 - Exit")
            ch = int(input("Your choice : "))
            if ch == 1:
                writeToFile()
            elif ch == 2:
                readFromFile()
            elif ch == 3:
                SearchById()
            elif ch == 4:
                updateRecord()
            elif ch == 5:
                deleteRecord()
            elif ch == 6:
                print("\n Thanks for using our System , we hope you like it :)")
                break
            else:
                print("\n please choose one of the shown choices\n")
        except Exception as e:
            print("Error occurred:", e)

main()
