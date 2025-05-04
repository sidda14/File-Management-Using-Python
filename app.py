import os   #os module is used to interact with the operating system and allows to perform tasks such as create,remove and rename files or directories

def create_file(fileName):  # method to create a new file
    try:
        with open(fileName, mode = 'x') as f:    #with method automatically closes the file when done and we do not need to write myFile.close(), 'x' is used when creating a file and it is created only when the file name doesn't already exist, as f meaning we assign the variable f to the file so we can use f.methodName() to perform operation on that file
            print(f"File Name {fileName}: Created Sucessfully!")
    except FileExistsError:   #if file already exists it will print the below statement
        print(f"File Name {fileName} already exists!")
    except Exception as E: #this can catch any exception that is present in the built in class Exception and assign the variable E to that exception object
        print ("An error occured!")

def view_all_files():  #method to view the files
    files = os.listdir()  #os.listdir() will give a list data structure and it will contain the names of all the files in this folder/directory
    if not files:  #if len(files) == 0, that is there are no files in the folder currently
        print("No file found!")
    else:
        print("Files in directory:")
        for file in files:  #prints the name of all the files in this directory
            print(file)

def delete_file(fileName):
    try:
        os.remove(fileName) #os.remove() will remove/delete the file from the directory
        print(f"{fileName} has been deleted successfully!")
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print("An error occured")

def read_file(fileName):
    try:
        with open(fileName, mode='r') as f:
         content = f.read()
         print(f"Content of '{fileName}' :\n{content}")

    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print("An error occured")

def edit_file(fileName):
    try:
        with open(fileName, mode = 'a') as f:
            content = input("Enter data to add:")
            f.write(content + "\n")
            print(f"Content added to {fileName} successfully")
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print("An error occured")

def main():
    while True:
        print("FILE MANAGEMENT APP")
        print("1: Create a file")
        print("2: View all files")
        print("3: Delete a file")
        print("4: Read a file")
        print("5: Edit a file")
        print("6: Exit")

        choice = input("Enter your choice (1-6): ")

        if(choice == '1'):
            fileName = input("Enter the file name to create: ")
            create_file(fileName)

        elif(choice == '2'):
            view_all_files()

        elif(choice == '3'):
            fileName = input("Enter the file name you want to delete: ")
            delete_file(fileName)

        elif(choice == '4'):
            fileName = input("Enter the file name you want to read: ")
            read_file(fileName)

        elif(choice == '5'):
            fileName = input("Enter the file name you want to edit:")
            edit_file(fileName)

        elif(choice == '6'):
            print("Closing the app......")
            break

        else:
            print("In valid syntax")

if __name__ ==  "__main__" : #checkingGithub
    main()




