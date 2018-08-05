spam =['apple', 'tofu', 'cat', 'pig']
def f(arr):
    s = ''
    for i in range(len(arr)):
        if i == 0:
            s = arr[i]
        elif i == len(arr) - 1:
            s = s + ',and ' + arr[i]
        else:
            s = s + ', ' +arr[i]
    print s
    
if __name__ == "__main__":
    f(spam)            
