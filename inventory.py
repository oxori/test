stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    item_total = 0
    print("inventory:")
    for x, y in inventory.items():
        print(str(y) + ' ', x)
        item_total += y
    print('Total number of items: ' + str(item_total))

def addToInventory(inventory, addedItems):
    for i in addedItems:
        stuff.setdefault(i, 0)
        stuff[i] = stuff[i] + 1
    return stuff

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

# displayInventory(stuff)
stuff = addToInventory(stuff, dragonLoot)
displayInventory(stuff)
