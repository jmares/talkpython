import random
print('---------------------------')
print('     M&M Guessing Game     ')
print('---------------------------')

print('Guess the number of M&Ms and you get luch on the house!')
print()

mm_count = random.randint(1, 100)
attempt_limit = 5
attempts = 0

while attempts < attempt_limit:
    guess_text = input('How many M&Ms are in the jar? ')
    guess =int(guess_text)
    if mm_count == guess:
        print(f"You got a free lunch! It was {guess}.")
        break
    elif guess < mm_count:
        print('Sorry that is too LOW!')
    else:
        print('That is too HIGH!')
    attempts += 1

print(f"Bye, you're done in {attempts}! The correct guess was {mm_count}.")
