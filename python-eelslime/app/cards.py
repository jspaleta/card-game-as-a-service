try: from random_word import RandomWords
except: RandomWords = False
try: from .words import defaults as default_words
except: from words import defaults as default_words
try: from .words import personas as default_personas
except: from words import personas as default_personas
from datadog import statsd, initialize
import random

options = {
    'statsd_host':'127.0.0.1',
    'statsd_port':8125
}

initialize(**options)
def new_judge():
        personas = default_personas
        random.shuffle(personas)
        return personas[0]

@statsd.timed('new_cards')
def new_cards():
    try:
        # First lets try to draw new words from online
        r = RandomWords()
        words = r.get_random_words(hasDictionaryDef="true", includePartOfSpeech="noun")
        client.incr('new_cards.lookup')
    except Exception as e :
        # opps something went wrong, lets use backup words 
        # Use statsd counter here to monitor error_rate
        statsd.increment('new_cards.errors')
        words = default_words
        pass
    # Shuffle the words
    random.shuffle(words)
    return words[0:7]

def main():
    import time
    while True:
        time.sleep(0.05)
        print("Drawing cards") 
        print(new_cards())

if __name__ == "__main__":
    main()

