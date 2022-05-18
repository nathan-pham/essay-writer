from pynput.keyboard import Key, Listener, Controller

keyboard = Controller()
word_list = []
word = ""

with open("./words.txt") as f:
    word_list = f.read().strip().split('\n')

def autocomplete():
    global word

    for known in word_list:
        if len(word) >= 0.6 * len(known) and len(word) < len(known) and known.startswith(word):
            start, end = known.index(word) + len(word), len(known)
            keyboard.type(known[start:end])
            word = ""
            return

def on_press(key):
    global word

    try:
        word += key.char
        autocomplete()
    except AttributeError:
        if key in (Key.enter, Key.space):
            word = ""

def on_release(key):
    if key == Key.esc:
        return False

with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()