from os import path

__dirname = path.dirname(__file__)
resolve = lambda *paths: path.join(__dirname, *paths)

def import_text(filename):
    with open(resolve(filename), encoding="utf-8") as f:
        return f.read()

common = import_text("./words.txt").split('\n')
holmes = import_text("./sherlock_holmes.txt")