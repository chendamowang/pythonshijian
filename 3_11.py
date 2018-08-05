def f():
    while True:
        s = raw_input("Enter number:\n")
        try: 
            num = int(s)
            break
        except ValueError:
            print "Please enter a number"
        #s = raw_input("Enter the number:")
    
    while num!= 1:
        print Collatz(num)
        num = Collatz(num)


def Collatz(num):
    if num % 2 == 0:
        return  num //2
    else:
        return 3 * num + 1
        
if __name__ == "__main__":
    f()
