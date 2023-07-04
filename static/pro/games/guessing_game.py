

secret_word = "abdo"

guess = ""

guess_count = 0
guess_limit = 5
out_of_guess = False

while guess != secret_word and not out_of_guess :

    if guess_count < guess_limit :
        guess = input("Enter guess word: ")
        guess_count += 1

    else :
        out_of_guess = True

if out_of_guess :
    print('you lose out of guesses')
else :
    print("you won")
