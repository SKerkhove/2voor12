from random import randint
import PySimpleGUI as sg
import os.path


def readwords():
    words = []
    with open('8letterwords.txt', 'r') as file:
        # reading each line
        for line in file:
            words = words + line.split()
    return words


def pickword(wordlist):
    num = randint(0, len(wordlist) - 1)
    return wordlist[num]


def prepword(word, game):
    letters = list(word)
    mirrorTrue = randint(0, 1)
    if mirrorTrue == 1:
        letters.reverse()
    rotate = randint(0, 7)
    letters = letters[rotate:] + letters[:rotate]
    if game == 0:
        missing_letter_num = randint(0, 7)
        missing_letter = letters[missing_letter_num]
        letters[missing_letter_num] = "?"
    else:
        missing_letter = None
    return letters, missing_letter


def makeTaart(letters):
    if len(letters) != 8:
        print("Invalid word, try again")
        return
    else:
        print("\t", letters[0], "\t", letters[1], "\t")
        print(" ", letters[7], "\t", "\t", letters[2], " ")
        print(" ", letters[6], "\t", "\t", letters[3], " ")
        print("\t", letters[5], "\t", letters[4], "\t")


def makePaardensprong(letters):
    if len(letters) != 8:
        print("Invalid word, try again")
        return
    else:
        return " " + letters[0] + "\t" + letters[3] + " \t" + letters[6] + "\n " + letters[5] + '\t \t' + letters[
            1] + "\n " + letters[2] + "\t" + letters[7] + " \t" + letters[4]


def taart(words):
    word = pickword(words)
    letters, missing_letter = prepword(word, 0)
    makeTaart(letters)
    return word, missing_letter


def paardensprong(words):
    word = pickword(words)
    letters, _ = prepword(word, 1)
    makePaardensprong(letters)
    return word


# First the window layout in 2 columns


if __name__ == '__main__':
    words = readwords()
    word = pickword(words)
    letters, _ = prepword(word, 1)
    # Create the window
    layout = [[sg.Text(makePaardensprong(letters))], [sg.Button("Antwoord")]]
    window = sg.Window("Demo", layout)

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "Antwoord":
            popup = sg.Window("Antwoord", [[sg.Text(word)],[sg.Button("Nieuwe puzzel")]])
            while True:
                event, values = popup.read()
                if event == "Nieuwe puzzel" or event == sg.WIN_CLOSED:
                    break
        if event == sg.WIN_CLOSED:
            break

    window.close()
