import os

#Search reading file
fname = input('Enter the file name: ')
try:
    if fname == 'na na boo boo':
        print("NA NA BOO BOO TO YOU - You have been punk'd! \n")
        exit()
    fhand = open(fname)
except:
    print('File cannot be opened: ', fname)
    exit()

count = 0

for line in fhand:
    count = count + 1
print('There were', count, 'subject lines in', fname)



os.system('exit')