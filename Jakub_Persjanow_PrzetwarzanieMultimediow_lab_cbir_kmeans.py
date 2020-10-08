"""
Przetwarzanie multimediów
PG, FTIMS
sem. 2019/2020
"""


import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial import distance 
%matplotlib


#Przyklady obliczeń odleglosci 
distance.euclidean([1,2,3],[3,4,5])
distance.cityblock([1,2,3],[3,4,5]) # cityblock = manhattan
# w rozwiązaniu zamiast przykładowych wektorów [1,2,3], które podałem wyżej będziecie Państwo wykorzystywali
# wektory cech obrazów, czyli histogramy unormowane.

# =============================================================================
# 
# Zadanie 
# Zbuduj prosty system wyszukiwania obrazów (CBIR), w ktorym dla kazdego obrazu wzorca (czyli tego obrazu, k
# do którego należy znaleźć obraz najbardziej podobny)
# zostanie przypisana lista 5 obrazów najbardziej podobnych według przyjętej miary odleglosci.
# W rozwiazaniu wykorzystaj metryki euklidesową oraz Manhattan (cityblock) - patrz wyżej.

# Pracuj na zbiorze obrazów umieszczonych w lokalizacji http://wang.ist.psu.edu/docs/related/ 
# (na stronie sa dwa zbiory do pobrania, wybierz ten, który zawiera 1000 obrazów).
# Taki zbiór będzie pełnił rolę Twoej bazy danych obrazów. Możesz pracować z wszystkimi pobranymi obrazami 
# lub z ich podbzbiorem. W tym drugim przypadku w podzbiorze musi być co najmniej 100 obrazów, po 10 obrazów z każdej
# kategorii tematycznej (łatwo zauważyć, że pobrane obrazy są tematycznie posortowane; w każdej kategorii jest 100 obrazów)
# 
# Obrazy powinny być reprezentowane unormowanymi histogramami RGB obrazów skwantyzowanych 
# skalarnie (dla zadanego stopnia kwantyzacji).

# Rozwiązanie zbuduj tak żeby można było je łatwo przetestować. Powinna być możliwosc wskazania w kodzie lub konsoli
# nazwy folderu z obrazami oraz nazwy lub numeru obrazu wzorcowego. W odpowiedzi na ekranie powinny zostać wyswietlone obrazy
# najbardziej podobne.
#
# Rozwiązanie powinno przebiegać według następującego ogólnego schematu
# 1. wczytanie obrazów
# 2. wykonanie na wszystkich obrazach kwantyzacji skalarnej np. do 8 poziomów na każdy z kanałów RGB --> w takim przypadku 
#   kwantyzacja powoduje ze każdy piksel będzie mógł przyjąć jedną z 8^3 możliwych wartosci (to tylko przyklad). 
#   Wykonanie kwantyzacji skalarnej jest konieczne i wynika z usunięcia szumu informacyjnego w obrazach
# 3. wyznaczenie dla każdego z obrazów histogramu RGB. Histogram tego typu to nic innego jak struktura danych przechowująca
#   liczbę wystąpień każdej z 8^3 możliwych kombinacji wartosci RGB. Przykladowy histogram może byc wektorem o długosci 512 
#   elementów o postaci: (0,100,200,0,10,30,...,0). Podany przeze mnie przyklad to oczywiscie histogram nieunormowany.
#   który posiada łatwą interpretację: "jest 0 pikseli (0,0,0); jest 100 pikseli (0,0,1); jest 200 piksel (0,0,2)..." itd.
# 4. dla przyspieszenia obliczeń i testowania wyznaczenie macierzy kwadratowej wymiaru 512 x 512 (wymiary podaje dla mojego przykladu 
#   kwantyzacji do osmiu wartosci na kanał - u Państwa może to być inaczej), której element a_ij przechowuje odległosc 
#   wektora cech "i-tego" obrazu do obrazu "j-tego". Wiersz "i-ty" takiej macierzy to nic innego jak zapisane odleglosci
#   "i-tego" obrazu do każdego obrazu z bazy danych. Oczywicie główna przekątna macierzy będzie zerowa oraz macierz jest symetryczna
#   ponieważ odległoć "i-tego" obrazu do "j-tego" jest taka sama jak "j-tego" do "i-tego".
# 5. w fazie testowania (własciwej pracy aplikacji) po podaniu numeru obrazu wzorcowego powinno nastąpić przeszukwanie
#   numeru wiersza takiej macierzy odpowiadającego poszukiwanemu obrazowi oraz zidentyfikowanie tych elementów w wierszu
#   macierzy, które mają najmniejszą wartosć -> są to odleglosci do najbardziej podobnych obrazów w bazie.
# =============================================================================


