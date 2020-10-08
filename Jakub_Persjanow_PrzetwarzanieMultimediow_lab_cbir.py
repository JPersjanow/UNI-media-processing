# -*- coding: utf-8 -*-
"""
Przetwarzanie multimediów
Laboratorium
PG, FTIMS
sem. 2019/2020
"""

import matplotlib.pyplot as plt
import numpy as np
%matplotlib  qt

#Pobierz 1000 obrazów ze strony http://wang.ist.psu.edu/docs/related/

# =============================================================================
# Ćwiczenie 1
# Kwantyzacja skalarna równomierna
# Uwaga: zmień scieżki dostępu do obrazów - zostawiłem je dla przejrzystoci kodu
# Przeanalizuj kod. Konieczne jest zrozumienie wykonywanych operacji!!
# =============================================================================


img = plt.imread('C:\\Users\\wilcz_m\\Desktop\\Dokumenty TMP\\obrazy\\200.jpg')
plt.imshow(img)

imglist=[]
for i in range(0,10):
    x = np.random.randint(0,1000)
    pth = "C:\\Users\\wilcz_m\\Desktop\\Dokumenty TMP\\obrazy\\"+str(x)+".jpg"
    print(pth)
    img = plt.imread(pth)
    imglist.append(img)


plt.close()
f,ax = plt.subplots(1,10,sharey = True,figsize = (25,25))
for i in range(0,10):
    ax[i].imshow(imglist[i]) 

#Klasteryzacja skalarna równomierna
img = plt.imread('C:\\Users\\wilcz_m\\Desktop\\Dokumenty TMP\\obrazy\\0.jpg')
plt.imshow(img)

#Dzięki wektoryzacji kwantyzację można wykonać bez jawnego wykonywania petli po elementach obrazu

imgq2 = np.floor(img/128)*128+64
imgq2 =imgq2.astype(int)

imgq4 = np.floor(img/64)*64 + 32
imgq4 = imgq4.astype(int)

plt.close()
f,ax = plt.subplots(1,3,sharey=True)
ax[0].imshow(img)
ax[1].imshow(imgq2)
ax[2].imshow(imgq4)            

# =============================================================================
# Cwiczenie 2
# Klasteryzacja kmeans (wektorowa) w przestrzeni RGB
# Klasteryzacja kmeans została opisana w wykładzie dotyczącym kwantyzacji - patrz slajdy 31 - 34 (tam oznaczona jako algorytm LGB)
# W pythonie algorytm kmeans wykonywany jest przy pomocy jednej instrukcji - KMeans, z parametrem odpowiadającym liczbie 
# klastrów.
# =============================================================================
from sklearn.cluster import KMeans

img = plt.imread('C:\\Users\\wilcz_m\\Desktop\\Dokumenty TMP\\obrazy\\0.jpg')
img2 = img.copy()
plt.imshow(img2)

img2 = img2.reshape(img2.shape[0]*img2.shape[1],3).copy()
img2.shape

kmeans = KMeans(n_clusters = 8)
kmeans.fit(img2)

#Oryginalnie srodki klastrow sa liczbami zmiennoprzecinkowymi (float). Dla funkcji imshow
#konieczna jest konwersja na int
kmeans.cluster_centers_ = np.floor(kmeans.cluster_centers_).astype(int)
kmeans.labels_

#Stworzenie wektora danych, w ktorych oryginalny punkt danych RGB jest zastąpiony centrum klastra, do ktorego
#taki punkt zostal zaliczony
img3 = kmeans.cluster_centers_[kmeans.labels_]
img.shape
img3 = img3.reshape(384,256,3)
img3.shape

plt.close()
f,ax = plt.subplots(1,2,sharey=True)
ax[0].imshow(img)
ax[1].imshow(img3)




# =============================================================================
# Budowa histogramu
# =============================================================================
#Przypomnienie dictionary comprehensions
hist = {i: 'liczba'+str(i) for i in range(0,10)}

for k,v in hist.items():
    print(k,v)

#slownik, ktorego kluczem jest krotka. To juz prawie struktura danych
# w ktorej chcielibysmy przechowywać histogram obrazu RGB
hist = {(i,j): 'liczba'+str(i)+","+str(j) for i in range(0,10) for j in range(0,10)}
hist

#inny slownik, ktorego kluczami jest krotka.
#klucz dostosowany do obrazu RGB skwantyzowanego do 4 poziomów na każdy z kanałów (dopuszczalnymi wartosciami w kanale są: 0,1,2,3)
hist = {(i,j,k): 0 for i in range(0,4) for j in range(0,4) for k in range(0,4)}

#aktualizacja histogramu
img = plt.imread('C:\\Users\\wilcz_m\\Desktop\\Dokumenty TMP\\obrazy\\0.jpg')
img2 = img.copy()
img2 = np.floor(img2/64).astype(int)
img2 = img2.reshape(256*384,3)
for i in range(0,img2.shape[0]):
    hist[img2[i,0],img2[i,1],img2[i,2]] = hist[img2[i,0],img2[i,1],img2[i,2]] + 1
    
#zbudowany histogram obrazu
#sprawdzmy, czy dane w histogramie mają sens
len(hist.keys()) #ok. dlugosc 64 elementy (=wektor w przestrzeni 64-wymiarowej)
len(hist.values()) 
np.sum(list(hist.values())) == 256*384  #suma liczby wystapien kazdej dopuszczalnej kombinacji RGB jest = liczbie pikseli --> OK

for k,v in hist.items():
    print(k,v)

#od tego momentu histogram jest wektorem 64 wymiarowym, który żyje w przestrzeni 64 wymiarowej
hist_vec = np.array(list(hist.values()))
len(hist_vec)
hist_vec

# =============================================================================
# 
# Zadanie
# Wykonaj klasteryzację obrazów w przestrzeni histogramow obrazów. 
# W takim przypadku histogram jest deskryptorem obrazu. 
# Zadanie powinno być wykonane na zbiorze lub podzbiorze obrazow http://wang.ist.psu.edu/docs/related/, 
# przy czym liczba obrazow musi być >=100 (co najmniej po 10 obrazów z każdej z 10 kategorii tematycznych).
# Wynikiem powinno być wyswietlenie wszystkich obrazow należących do poszczególnych zbudowanych przez metodę 
# klastrów.
# Sprawdź i oceń, czy taka metoda klasteryzacji grupuje tematycznie obrazy. Opisz to w komentarzu do wykonanego zadania.
# Do rozwiązania niezbędne jest wykonanie następujących etapów (w oparciu np. o kod powyżej)
# 1. wczytanie obrazów
# 2. kwantyzacja skalarna
# 3. wyznaczenie histogramów wszystkich obrazów
# 4. wykonanie kwantyzacji kmeans w przestrzeni histogramów obrazów skwantyzowanych skalarnie. To ważne!!
# Uwaga: wynikiem kwantyzacji będzie przyporządkowanie każdemu histogramowi nr klastra. Na tej podstawie, np. 
# wywietlając obrazy z danego klastra widać, czy algorytm "sensownie" pogrupował do jednego klastra obrazy tematycznie podobne.
# =============================================================================


