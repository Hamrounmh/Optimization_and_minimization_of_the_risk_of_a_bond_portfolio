import math

from appJar import gui
import numpy as np


def truncate(f, n):
    return math.floor(f * 10 ** n) / 10 ** n


def treillis(actifPrice, strike, taux, up, down, periode, optionType, optionOrigine):
    # init the matrix
    global columnValue
    m = periode * 2 + 1
    n = periode
    matrix = np.zeros((m, n + 1))
    # init the call put situation
    clefCallPut = -1
    if optionType == "PUT":
        clefCallPut = 1

    # calculate probabilities pU and pD
    ratio = 1 + taux
    pU = (ratio - down) / (up - down)

    tauxRatio = 1 / ratio

    # calculate the first elements
    j = m - 1
    i = 0
    while j >= 0:
        actifAtT = ((up ** i) * (down ** (n - i)) * actifPrice)
        value = strike - actifAtT
        valueN = max(value * clefCallPut, 0)
        matrix[j][periode] = valueN
        j = j - 2
        i = i + 1
    # calculate the rest of the elements with reccurence
    n = n - 1
    i = 1
    while n >= 0:
        j = (periode * 2) - i
        h = n + 1
        k = 0
        while j >= 0:
            columnValue = (1 / 1 + taux) * ((1 - pU) * matrix[j + 1][n + 1] + (pU) * matrix[j - 1][n + 1])
            if optionOrigine == "USA":
                if optionType == "PUT":
                    amiricaineValue = strike - ((up ** (j+1)) * (down ** (periode - (j+1))) * actifPrice)
                    columnValue = max(columnValue, amiricaineValue)

            matrix[j][n] = columnValue
            j = j - 2
            k = k + 1
            if k == h:
                break

        n = n - 1
        i = i + 1

    return (matrix,columnValue)


def treilli_slove():
    return 0


def MyTableFormatter():
    tablen = len(app.getTableRow("g1", 0))
    liste = []
    for i in range(tablen):
        liste.append('T=' + str(i))
    app.replaceTableRow("g1", -1, liste)
    length = app.getTableRowCount("g1")
    for i in range(length):
        tab = app.getTableRow("g1", i)
        for j in range(len(tab)):
            if tab[j] == '0.0':
                tab[j] = '  '
        app.replaceTableRow("g1", i, tab)


def press(button):
    if button == "Cancel":
        app.stop()
    else:
        actifPrice = float(app.getEntry("Action price"))
        strike = float(app.getEntry("Strike"))
        taux = float(app.getEntry("Taux"))
        up = float(app.getEntry("Up frequency"))
        down = float(app.getEntry("Down frequency"))
        periode = int(app.getEntry("Periodes"))
        optionType = app.getRadioButton("OptionTypeRadio")
        callPut = app.getRadioButton("CallPut")

        matrix, vo = treillis(actifPrice, strike, taux, up, down, periode, callPut, optionType)

        if periode < 30:
            try:
                app.addTable("g1", matrix)
                result = "le prix de l'option est : " + str(truncate(vo, 2))
                app.setLabel("result", result)
            except:
                app.replaceAllTableRows("g1", matrix, deleteHeader=True)
                result = "le prix de l'option est : " + str(truncate(vo, 2))
                app.setLabel("result", result)
            MyTableFormatter()

        else:
            # app.deleteAllTableRows("g1")
            result = "le prix de l'option est : " + str(truncate(vo, 2))
            app.setLabel("result", result)


###########################################


app = gui()

# add & configure widgets - widgets get a name, to help referencing them later
app.addLabel("title", "Welcome to Option pricing")
app.setLabelBg("title", "red")

# zones de textes
app.addLabelEntry("Action price")
app.addLabelEntry("Strike")
app.addLabelEntry("Up frequency")
app.addLabelEntry("Down frequency")
app.addLabelEntry("Periodes")
app.addLabelEntry("Taux")

# boutons radios

app.addRadioButton("CallPut", "PUT")
app.addRadioButton("CallPut", "CALL")

app.addRadioButton("OptionTypeRadio", "EUR")
app.addRadioButton("OptionTypeRadio", "USA")

app.addEmptyLabel("result")

# link the buttons to the function called press
app.addButtons(["Submit", "Cancel"], press)

# start the GUI
app.go()

# (matrix, vo) = treillis(100, 98, 0.00077, 1.0425, 0.9592, 10, "PUT", "USA")
# print(vo)
