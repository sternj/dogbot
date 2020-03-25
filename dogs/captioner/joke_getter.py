import requests
from nltk.tokenize import sent_tokenize
from typing import List
def get_random_joke() -> str:
    x = requests.get('https://icanhazdadjoke.com', 
        headers={'Accept': 'text/plain'})

    return x.content.decode('utf-8')

def get_joke_of_right_length() -> List[str]:
    while True:
        joke = get_random_joke()
        tok_joke = sent_tokenize(' '.join(joke.split()))
        if len(tok_joke) == 2:
            return tok_joke