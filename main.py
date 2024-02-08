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

def prepword(word):
    letters = list(word)
    mirrorTrue = randint(0,1)
    if mirrorTrue == 1:
        letters.reverse()
    rotate = randint(0,7)
    letters = letters[rotate:] + letters[:rotate]
    missing_letter_num = randint(0,7)
    missing_letter = letters[missing_letter_num]
    letters[missing_letter_num] = "?"
    # missing_letter = ""
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


if __name__ == '__main__':
    words = readwords()
    while True:
        word = pickword(words)
        letters, missing_letter = prepword(word)
        makePaardensprong(letters)

        ans = input("See solution?")
        if ans != None:
            print("The missing letter was ", missing_letter, word)

        again = input("New puzzle?"
                      "\n\t(0) Yes"
                      "\n\t(1) No\n")
        if int(again) == 1:
            break