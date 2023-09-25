print('Warm Up\n'.upper())


def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3, '\n')


row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']

display(row1, row2, row3)

row2[1] = 'X'

display(row1, row2, row3)

# position_index = int(input('choose an index position: '))
# row1[position_index] = input('enter value: ')
display(row1, row2, row3)


def user_choice():
    choice = 'wrong!'
    acceptable_range = range(0, 10)
    within_range = False
    while choice.isdigit() == False or within_range == False:

        choice = input('Please enter number (1-10): ')
        if not choice.isdigit():
            print('Sorry that is not a digit!')
        if choice.isdigit():
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print('Sorry digit is not in range')
                within_range = False

    return int(choice)


print('user digit is: ', user_choice())
user_choice()
