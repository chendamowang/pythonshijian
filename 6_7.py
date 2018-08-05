tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


m = len(tableData)
n = len(tableData[0])
colWidths = [0] * m

def f(i):
    max = 0 
    for j in tableData[i]:
        if len(j) > max :
            max = len(j)
    colWidths[i] = max

for i in range(m):
    f(i)

def printTable(table, width):
    for i in range(n):
        for j in range(m):
            if j != m - 1:
                print table[j][i].rjust(width[j]),
            else:
                print table[j][i].rjust(width[j])

if __name__ == '__main__':
    printTable(tableData, colWidths)                  
