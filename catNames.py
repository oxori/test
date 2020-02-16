cat_names = []
while True:
    print('%s%s' % ('Enter the name of your cat No: ', len(cat_names) + 1))
    name = input()
    if name == '':
        break
    cat_names = cat_names + [name]

for i in cat_names:
    print(i)
