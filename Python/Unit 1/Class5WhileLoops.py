# counter = 0

# while (counter < 100):
#     print('eat poop', counter)
#     counter += 1

# print('Done')

ated_poop = False

while ated_poop == False:
    print('Do you eat the poop?')
    answer = input('Yes or No: ')

    if (answer.strip().lower() == 'yes'):
        print('eats poop')
        print('poop good')
        print('poop')
        ated_poop = True
    elif (answer.strip().lower() == 'no'):
        print('You did not eat the poop')
    else:
        print('You fail')

print('Done')