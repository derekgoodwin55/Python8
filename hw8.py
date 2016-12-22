### Header ###
print("Airport Routing Filter")
import os

### Prompt file open. After 3 incorrect attempts, system terminates ######
def openfile():
    
    tries = 3

    while tries > 0:
        filename = input("Enter the source file name: ")
        valid = False

        try:
            original = open(filename,'r')
            valid = True

        except FileNotFoundError:
            print("File not found.", tries - 1, "attempts remaining.")
            tries -= 1

            if tries == 0:
                print("System Terminated")
                raise SystemExit

        if valid == True:
            return original

    return None

### openfile Function Call & Output File Creation ###
routes = openfile()

output = str(input("Enter the output file name: "))

if os.path.isfile(output) == True:
    exist = str(input("File Exists... overwrite? (y/n): "))
    if exist.lower() == "y":

        new = open(output, "w")
   
### Function ###

        prompt = str(input("Enter airport symbol: "))

        while routes.readline() != "":
            line = routes.readline()
            if prompt.lower() in line or prompt.upper() in line:
                new.write(line)
        print("Finished")
        new.close()

    else:
        print("Overwrite declined. System Terminated")
### Close Both files ###
routes.close()
