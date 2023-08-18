def addNumber():
    lst = [0]
    userNumber = 0

    while (True):
            userNumber = input("enter a number to add ")
            if userNumber == "x":
                print(lst)
                print(lst.count)
                break
            else:
                lst.append(userNumber)
                print(lst)

if __name__== '__main__':
    addNumber()
