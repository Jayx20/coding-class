import random

# By Jordan, Maddy, Mark, Marshall, Nick

# 0 = rock/boulder
# 1 = paper/parchment
# 2 = scissors/shears

# no modular math for this particular problem, but maybe for a future similar problem.
# no machine learning
# ai will pick randomly between the three at 33% chance each

counter=0
game_over = False

while not game_over:
    choice_integer = -1
    computer_choice = random.randint(0, 2)
    while choice_integer == -1:
        player_choice = input('Boulder, Parchment, or Shears: ').strip().lower()

        if player_choice == 'boulder':
            choice_integer = 0
        elif player_choice == 'parchment':
            choice_integer = 1
        elif player_choice == 'shears':
            choice_integer = 2
        else:
            print('YOU FAIL')

    if choice_integer == 0:
        # player picked boulder
        if computer_choice == 0:
            # computer put boulder
            print('Computer picks boulder!')
            print('It\'s a tie! Try again.')
        elif computer_choice == 1:
            # computer put parchment
            print('Computer picks parchment!')
            print('Parchment beats boulder! You FAIL.')
            game_over = True
        elif computer_choice == 2:
            # computer put shears
            print('Computer picks shears!')
            print('Shears loses to parchment! You WIN.')
            counter += 1
    elif choice_integer == 1:
        # player picked parchment
        if computer_choice == 0:
            # computer put boulder
            print('Computer picks boulder!')
            print('Parchment eats boulders ass! You WIN?')
            counter += 1
        elif computer_choice == 1:
            # computer put parchment
            print('Computer picks parchment!')
            print('Parchment and parchment are the same thing! It\'s a tie.')
        elif computer_choice == 2:
            # computer put shears
            print('Computer picks shears!')
            print('Shears shred yo ass! You FAIL.')
            game_over = True
    elif choice_integer == 2:
        # player picked shears
        if computer_choice == 0:
            # computer put boulder
            print('Computer picks boulder!')
            print('Boulder whips and nae nae\'s on shears. You FAIL!')
            game_over = True
        elif computer_choice == 1:
            # computer put parchment
            print('Computer picks parchment!')
            print('Shears shears parchment! You WIN!')
            counter += 1
        elif computer_choice == 2:
            # computer put shears
            print('Computer picks shears!')
            print('It\'s shearley a tie.')

    if counter == 10:
        print('HALF MORB ACTIVATED.')
    if counter == 69:
        print('YOU HAVE REACHED FULL MORB. GOING MORBIUS MODE.')
        game_over = True

print('The End!')
input()