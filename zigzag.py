import time

cnt = 0
blank = ' '
indentIncreasing = True
while True:
    if indentIncreasing:
        idt = blank * cnt
        print('%s%s' % (idt, '********'), end='\n')
        cnt += 1
        time.sleep(0.1)
        if cnt == 15:
            indentIncreasing = False
    else:
        idt = blank * cnt
        print('%s%s' % (idt, '********'), end='\n')
        cnt -= 1
        time.sleep(0.1)
        if cnt == 0:
            indentIncreasing = True
