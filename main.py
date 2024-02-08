from random import randint


def readwords():
    words = []
    with open('8letterwords.txt', 'r') as file:
        # reading each line
        for line in file:
            words = words + line.split()
    return words


def pickword(wordlist):
    num = randint(0, len(wordlist)-1)
    return wordlist[num]

def prepword(word, game):
    letters = list(word)
    mirrorTrue = randint(0,1)
    if mirrorTrue == 1:
        letters.reverse()
    rotate = randint(0,7)
    letters = letters[rotate:] + letters[:rotate]
    if game == 0:
        missing_letter_num = randint(0,7)
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
        print(" ", letters[7], "\t", "\t", letters[2]," ")
        print(" ", letters[6], "\t", "\t", letters[3]," ")
        print("\t", letters[5], "\t", letters[4], "\t")

def makePaardensprong(letters):
    if len(letters) != 8:
        print("Invalid word, try again")
        return
    else:
        print(" ", letters[0], "\t", letters[3], " \t", letters[6])
        print(" ", letters[5], "\t \t \t", letters[1])
        print(" ", letters[2], "\t", letters[7], " \t", letters[4])

def taart(words):
    word = pickword(words)
    letters, missing_letter = prepword(word,0)
    makeTaart(letters)
    return word, missing_letter

def paardensprong(words):
    word = pickword(words)
    letters, _ = prepword(word,1)
    makePaardensprong(letters)
    return word

if __name__ == '__main__':
    words = readwords()
    ans1 = input("Welk spel wil je spelen?"
                 "(0) Taartpuzzel"
                 "(1) Paardensprong")

    while True:
        if int(ans1) == 0:
            word, missing_letter = taart(words)

            ans = input("Druk op enter voor de oplossing")
            if ans != None:
                print("De ontbrekende letter was ", missing_letter,"\n", word)
        if int(ans1) == 1:
            word = paardensprong(words)
            ans = input("Druk op enter voor de oplossing")
            if ans != None:
                print("Het antwoord is ", word)

        again = input("Nieuwe puzzel?"
                      "\n\t(0) Ja"
                      "\n\t(1) Nee\n")
        if int(again) == 1:
            break