n1 = int(input("enter a number "))
n2 = int(input("another number "))

def findBigger():
    if n1 > n2:
        print(n1,"is bigger!")
    else:
        print(n2,"is bigger!")

if __name__== '__main__':
    findBigger()