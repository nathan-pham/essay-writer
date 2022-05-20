from pynput.keyboard import Key, Listener, Controller
from corpus.text import common
from markov import markov
from re import sub

keyboard = Controller()
word = ""

def autocomplete():
    global word

    for known in common:
        if len(word) >= 0.6 * len(known) and len(word) < len(known) and known.startswith(word):
            start, end = known.index(word) + len(word), len(known)
            keyboard.type(known[start:end])
            word = ""
            return

def on_press(key):
    global word

    try:
        if key.char is not None and key.char.isalpha():
            word += key.char
    except AttributeError:
        if key == Key.space and len(word) > 0:
                generated = markov.generate_word(sub('\W+', '', word))
                word = ""

                if generated:
                    keyboard.type(generated)

def on_release(key):
    if key == Key.esc:
        return False

with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()