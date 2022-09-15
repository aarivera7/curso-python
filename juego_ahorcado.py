import platform
import random
import os

def run(): 
    try:
        with open("./archivos/datos.txt", "r", encoding="utf-8") as f:
            words = [line.strip() for line in f]
    except FileNotFoundError:
        print("Error fatal no se encontro un archivos con las palabras requeridas.")
        exit(0)
    
    idx = random.randint(0, len(words) -1)
    word = words[idx]
    size = len(word)
    count = 0
    str = " "
    letters = [{"letter": i, "found": False} for i in word]

    while count != size:
        for i in letters:
            if i["found"]:
                str += i["letter"] + " "
            else:
                str += "_ "

        print("¡Adivina la palabra!")
        print(str+"\n")
        letter = input("Ingrese una letra: ").strip()

        try:
            assert len(letter) == 1 and not letter.isnumeric(), "Error no haz ingresado una letra."
        except AssertionError:
            cleanConsole()
            print("Error no haz ingresado una letra.")
            str = " "
            continue

        for i in letters:
            if i["letter"] == letter and not i["found"]: 
                i["found"] = True
                count += 1
                
        str = " "
        cleanConsole()

    print("Ganaste la palabra era "+word)

def cleanConsole():
    if platform.system() == 'Windows':
        os.system("cls")
    else:
        os.system("clear")

if __name__ == "__main__":
    run()