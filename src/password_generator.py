import random
import nltk
from nltk.corpus import words


# use random to randomly pick a word from list
# sample grabs words and puts in a list

# make hard password but made out of words, easier to remmeber, instead of random chars

# can user input be added


def generate_random_password():
    try:
        word_list = words.words()
    except LookupError:
        nltk.download('words')

    while True:
        try:
            word_amount = int(input("Suggest word amount (2, 3, or 4): "))
            if word_amount in [2, 3, 4]:
                break
            else:
                print("Only 2, 3, or 4 are accepted.")
        except ValueError:
            print("Please enter a valid number.")

    generated_password = ""
    # 'randoms' of variables
    random_words = random.sample(word_list, word_amount)
    special_chars = "!@#$%&?"
    random_special_char = random.choice(special_chars)

    for word in random_words:
        word = word.title()  # caps first letter of word
        generated_password += word  # appends each word while irritation goes on
        number = random.randint(0, 9)  # chooses random number
        generated_password += str(number)

    generated_password += random_special_char  # ends with special char

    if len(generated_password) >= 16:  # checks if length is 16 cuz 16 is strong
        print(generated_password)
    else:
        return generate_random_password()  # if not makes another passw


if __name__ == "__main__":
    generate_random_password()
