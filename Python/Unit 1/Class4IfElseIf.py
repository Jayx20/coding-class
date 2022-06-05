# boolin = True
# marshalls_boolin = False

# if marshalls_boolin:
#     print('eats poop')
#     print('poop good')
#     print('poop')
# print('joe')

print('Do you eat the poop?')
answer = input('Yes or No: ')

if (answer.strip().lower() == 'yes'):
    print('eats poop')
    print('poop good')
    print('poop')
elif (answer.strip().lower() == 'no'):
    print('You did not eat the poop')
else:
    print('You fail')

print('Done')