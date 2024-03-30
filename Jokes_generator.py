import requests
import json
import random

# Lists of phrases or closings for responses within the program
phrases = ['Great', 'Awesome', 'Wonderful', 'Here is a really funny one']
closings = ["We have 100's of jokes, so please come back when you need a good laugh.",
            "You didn't like that joke? Maybe they will be funny later. Thanks for checking us out.",
            "They all cannot be great, but I am hoping you liked at least one. Thanks for visiting."]


def main():
    """Main function for the program. Allows for user to receive a joke or not and if they
    would like to receive another joke"""
    option_1 = str(input('Would your like to hear a joke, Yes or No? ')).lower().strip()
    # while loop to allow for a yes selection or to exit the program (and to catch input errors)
    while not (option_1 == 'yes' or option_1 == 'no'):
        option_1 = str(input('You did not enter a valid selection, Yes or No are your only two options.\n'
                             'Please enter Yes or No to continue: ')).lower().strip()
    if option_1 == 'yes':
        print(f'{random.choice(phrases)}!')
        get_joke()
        print('')
        hear_another()
    if option_1 == 'no':
        print("We have 100's of jokes, so please come back when you need a good laugh.")


def get_joke():
    """Makes a GET request to the url, parses and displays the data"""
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.request("GET", url)
    parsed = json.loads(response.text)
    print(json.dumps(parsed["value"]))


def hear_another():
    """Allows the user to receive another joke or exit the program"""
    option_2 = str(input('Would you like to hear another joke, Yes or No? ')).lower().strip()
    # while loop to allow for a yes selection or to exit the program (and to catch input errors)
    while not (option_2 == 'yes' or option_2 == 'no'):
        option_2 = str(input('You did not enter a valid selection, Yes or No are your only two options.\n'
                             'Please enter Yes or No to continue: ')).lower().strip()
    if option_2 == 'yes':
        print(f'{random.choice(phrases)}!')
        get_joke()
        print('')
        main()
    if option_2 == 'no':
        print(f'{random.choice(closings)}')


print('Hello and Welcome to the Chuck Norris Joke Generator!')  # greeting to user
main()
