def main():
    # To open a file for writing/create that file if it does not already exist
    # myFile = open('file.txt', 'w+') 

    # To append data to an existing file
    myFile = open('file.txt', 'a')

    # To write to that now opened file
    for i in range(10):
        myFile.write("This is some text\n")

    # To close access to the file
    myFile.close()

    # To read data from the file
    myFile = open('file.txt', 'r')
    if myFile.mode == 'r':
        content = myFile.read()
    print(content)

    # To read more specifically
    if myFile.mode == 'r':
        fl = myFile.readlines()
        for x in fl:
            print(x)

    return 0

if __name__ == "__main__":
    main()