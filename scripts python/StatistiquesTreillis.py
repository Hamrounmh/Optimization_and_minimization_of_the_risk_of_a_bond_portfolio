import matplotlib.pyplot as plt
import time
import math
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

    return matrix, columnValue

#
n = 100
_temps_eur = []
_time_USA = []
series = []

for i in range(3, n):
    series.append(i)
    tempexc = time.time()
    (matrix, vo) = treillis(100, 98, 0.00077, 1.0425, 0.9592, i, "PUT", "USA")
    optionvalueUsa = vo
    tps_Us2 = time.time()
    _time_USA.append((tps_Us2 - tempexc) * 1000)



    tps_EUR1 = time.time()
    (matrix, vo_Eur) = treillis(100, 98, 0.00077, 1.0425, 0.9592, i, "CALL", "EUR")
    optionvalue_EUR = vo_Eur
    tps_EUR2 = time.time()
    _temps_eur.append((tps_EUR2 - tps_EUR1) * 1000)

plt.figure(figsize=(7.5,5)) #Changer taille de la figure
plt.plot(series, _time_USA, label='Option Américaine')
plt.plot(series, _temps_eur, label='Option Européenne')
plt.xlabel("Le nombre de periode N")
plt.ylabel("Temps d'execution en Milliseconds")
plt.legend(framealpha=2, frameon=True);
plt.show()

#
# #Le nombre de periode N:
n = 100
price_PutEu = []
price_Putus = []
series = []

for i in range(3, n):
    series.append(i)
    # Put
    mt, optionvalue_Put_USD = treillis(100, 98, 0.00077, 1.1, 0.9, i, "PUT", "USA")
    price_Putus.append(optionvalue_Put_USD)

    # Put
    mt, optionvalue_Put_Eur = treillis(100, 98, 0.00077, 1.1, 0.9, i, "CALL", "EUR")
    price_PutEu.append(optionvalue_Put_Eur)



plt.figure(figsize=(7.5,5))

plt.plot(series, price_Putus, label='PUT Américain')  # Plot l'EUR

plt.plot(series, price_PutEu, label='CALL Européen')  # Plot l'USD

plt.xlabel("Le nombre de periode N")
plt.ylabel("Prix de l'option ")
plt.legend(framealpha=1, frameon=True);
plt.show()
#
# #Varier les taux
# n = 100
# price_PutEu = []
# price_Putus = []
# series = []
# price_Call_USD = []
# price_Call_eur = []
# for i in range(1, 99):
#     x = 0.01+float(i/100)
#     r = x/52
#     series.append(x)
#
#     mt, optionvalue_Put_USD = treillis(100, 90, r, 1.1, 0.9, 10, "PUT", "USA")
#     price_Putus.append(optionvalue_Put_USD)
#
#
#     mt, optionvalue_Put_Eur = treillis(100, 90, r, 1.1, 0.9, 10, "PUT", "EUR")
#     price_PutEu.append(optionvalue_Put_Eur)
#
#     mt, optionvalue_Call_USD = treillis(100, 90, r, 1.1, 0.9, 10, "CALL", "USA")
#     price_Call_USD.append(optionvalue_Call_USD)
#
#
#     mt, optionvalue_Call_Eur = treillis(100, 90, r, 1.1, 0.9, 10, "CALL", "EUR")
#     price_Call_eur.append(optionvalue_Call_Eur)
#
#
# plt.figure(figsize=(7.5,5))
#
# plt.plot(series, price_Putus, label='PUT Américain')  # Plot l'EUR
#
# plt.plot(series, price_PutEu, label='PUT Européen')  # Plot l'USD
# plt.plot(series, price_Call_USD, label='CALL Américain')  # Plot l'EUR
#
# plt.plot(series, price_Call_eur, label='CALL Européen')  # Plot l'USD
#
# plt.xlabel("Le Taux de l'option r entre 1% et 100% ")
# plt.ylabel("Prix de l'option ")
# plt.legend(framealpha=1, frameon=True);
# plt.show()
#
#
# #Varier le  u
# n = 100
# price_PutEu = []
# price_Putus = []
# series = []
# price_Call_USD = []
# price_Call_eur = []
# for i in range(1, 100):
#     u = 2-float(i/100)
#     d = float(i/100)
#
#     series.append(u)
#     # Put
#     mt, optionvalue_Put_USD = treillis(100, 90, 0.00077, u, d, 10, "PUT", "USA")
#     price_Putus.append(optionvalue_Put_USD)
#
#     # Put
#     mt, optionvalue_Put_Eur = treillis(100, 90, 0.00077, u, d, 10, "PUT", "EUR")
#     price_PutEu.append(optionvalue_Put_Eur)
#
#     mt, optionvalue_Call_USD = treillis(100, 90,0.00077, u, d, 10, "CALL", "USA")
#     price_Call_USD.append(optionvalue_Call_USD)
#
#     # Put
#     mt, optionvalue_Call_Eur = treillis(100, 90, 0.00077, u, d, 10, "CALL", "EUR")
#     price_Call_eur.append(optionvalue_Call_Eur)
#
#
# plt.figure(figsize=(7.5,5))
#
# plt.plot(series, price_Putus, label='PUT Américain')  # Plot l'EUR
#
# plt.plot(series, price_PutEu, label='PUT Européen')  # Plot l'USD
# plt.plot(series, price_Call_USD, label='CALL Américain')  # Plot l'EUR
#
# plt.plot(series, price_Call_eur, label='CALL Européen')  # Plot l'USD
#
# plt.xlabel("Le taux de variation d'augmentation de l'option U  ")
# plt.ylabel("Prix de l'option ")
# plt.legend(framealpha=1, frameon=True);
# plt.show()
#
# #Varier le D
# n = 100
# price_PutEu = []
# price_Putus = []
# series = []
# price_Call_USD = []
# price_Call_eur = []
# for i in range(1, 100):
#     u = 2-float(i/100)
#     d = float(i/100)
#
#     series.append(d)
#     # Put
#     mt, optionvalue_Put_USD = treillis(100, 90, 0.00077, u, d, 10, "PUT", "USA")
#     price_Putus.append(optionvalue_Put_USD)
#
#     # Put
#     mt, optionvalue_Put_Eur = treillis(100, 90, 0.00077, u, d, 10, "PUT", "EUR")
#     price_PutEu.append(optionvalue_Put_Eur)
#
#     mt, optionvalue_Call_USD = treillis(100, 90,0.00077, u, d, 10, "CALL", "USA")
#     price_Call_USD.append(optionvalue_Call_USD)
#
#     # Put
#     mt, optionvalue_Call_Eur = treillis(100, 90, 0.00077, u, d, 10, "CALL", "EUR")
#     price_Call_eur.append(optionvalue_Call_Eur)
#
#
# plt.figure(figsize=(7.5,5))
#
# plt.plot(series, price_Putus, label='PUT Américain')  # Plot l'EUR
#
# plt.plot(series, price_PutEu, label='PUT Européen')  # Plot l'USD
# plt.plot(series, price_Call_USD, label='CALL Américain')  # Plot l'EUR
#
# plt.plot(series, price_Call_eur, label='CALL Européen')  # Plot l'USD
#
# plt.xlabel("Le taux de variation de baisse du produit :  D  ")
# plt.ylabel("Prix de l'option ")
# plt.legend(framealpha=1, frameon=True);
# plt.show()
