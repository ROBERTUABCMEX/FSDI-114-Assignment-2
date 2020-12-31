

def revert_word(word1, posicion):

    letra = word1[posicion]
    print(" %s " % letra)
    if posicion != 0:
        revert_word(word1, posicion-1)

def integer_list(intList):
    listreturn = []
    valor = 1
    for x in range(len(intList)):
        for z in range(len(intList)):
            if x != z:
                valor *= intList[z]
        listreturn.append(valor)
        valor = 1

    for x in range(len(listreturn)):
        print("%s" % int(listreturn[x]))
if __name__ == "__main__":

    word1 = "Roberto"
    revert_word(list(word1), len(word1)-1)
    print("--------------------------------------------------------")
    mylist = [1, 2, 3, 4]
    integer_list(mylist)
