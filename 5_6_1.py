# -*- coding: utf-8 -*-

stuff = {'arrow' : 12,
         'gold coin' : 42,
         'rope' : 1,
         'torch' : 6,
         'dagger' : 1}
dragonLoot = ['gold coin', ]
         
def displayInventory(arr):
    print "Inventory:"
    total = 0
    for k, v in arr.items():
        print str(v) + ' ' + k
        total += v
    print "Total number of items: %d" % (total)

def addToInventory(inventory, addedItems):
    for i in addedItems:
        if i in inventory:
            inventory[i] += 1
        else:
            inventory[i] = 1
    
    return inventory
    
if __name__ == '__main__':
    inv = {'gold coin' : 42, 'rope' : 1}
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    inv = addToInventory(inv, dragonLoot)
    displayInventory(inv)  
