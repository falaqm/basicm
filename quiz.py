def which_prize(num):
    if num<=50:
        prize='wooden rabbit'
    elif num <=150:
        prize=0
        print("Oh dear, no prize this time.")
    elif num<=180:
        prize='wafer-thin mint'
    elif num<=200:
        prize='penguin'
    else:
        prize=0
        print('wrong input')
    if prize:
        return print("Congratulations! You have won a {}!".format(prize))


while True:
    number=int(input('enter num,-999 for exit '))
    if number==-999:
        break
    which_prize(number)
