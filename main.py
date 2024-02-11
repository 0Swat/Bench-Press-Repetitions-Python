# Temat projektu: Wpływ 5 czynników na ilość powtózeń wyciskania
#
# Opis programu:
# Program symuluje wpływ różnych czynników (sen, poprzedni trening, kofeina, rozgrzewka, kontuzja barku)
# na ilość powtórzeń podczas treningu siłowego. Program generuje losowe dane na podstawie tych czynników
# i oblicza ilość powtórzeń, a następnie tworzy wykresy i histogramy dla analizy wyników.
#
# Uwaga: Waga oraz ilość powtórzeń zostały ustalone z góry - 74 kg, 15 powtórzeń. Można zmienić w programie kod aby zasymulować, z danymi wczytanymi podczas uruchamiania programu.
#
# ETAP 1 - SEN - ROZKŁAD DYSKRETNY:
# - Odpowiedź 1: Szansa < 0.25 (Spałeś mniej niż 6 godzin)
# - Odpowiedź 2: Szansa 0.25 - 0.50 (Spałeś między 6-7 godzin)
# - Odpowiedź 3: Szansa 0.50 - 0.75 (Spałeś między 8-9 godzin)
# - Odpowiedź 4: Szansa > 0.75 (Spałeś więcej niż 9 godzin)
#
# ETAP 2 - POPRZEDNI TRENING - ROZKŁAD DYSKRETNY:
# - Odpowiedź 1: Szansa < 0.05 (Wyciskałeś dzisiaj lub wczoraj)
# - Odpowiedź 2: Szansa 0.05 - 0.65 (Wyciskałeś od 2 do 3 dni temu)
# - Odpowiedź 3: Szansa 0.65 - 0.9 (Wyciskałeś od 4 do 7 dni temu)
# - Odpowiedź 4: Szansa > 0.9 (Wyciskałeś więcej niż 7 dni temu)
#
# ETAP 3 - KOFEINA - ROZKŁAD DYSKRETNY:
# - Odpowiedź 1: Szansa < 0.1 (Nie brałeś kofeiny przed treningiem)
# - Odpowiedź 2: Szansa 0.1 - 0.8 (Wziąłeś 200 mg kofeiny przed treningiem)
# - Odpowiedź 3: Szansa > 0.8 (Wziąłeś 400 mg kofeiny przed treningiem)
#
# ETAP 4 - ROZGRZEWKA - ROZKŁAD DYSKRETNY:
# - Odpowiedź 1: Szansa < 0.1 (Nie rozgrzewałeś się)
# - Odpowiedź 2: Szansa 0.1 - 0.55 (Rozgrzewałeś się między 15 a 30 minut)
# - Odpowiedź 3: Szansa 0.55 - 0.8 (Rozgrzewałeś się między 30 a 45 minut)
# - Odpowiedź 4: Szansa > 0.8 (Rozgrzewałeś się więcej niż 45 minut)
#
# ETAP 5 - KONTUZJA BARKU - ROZKŁAD CIĄGŁY (DLA PRAWDOPODOBIEŃSTWA):
# - Odpowiedź 1: Szansa < ~ 0.97 (Brak kontuzji barku)
# - Odpowiedź 2: Szansa > ~ 0.97 (Kontuzja barku - przerwanie wyciskania)
# // Szansa na kontuzje może się zwiększyć jeśli na etapie 2 lub 4 odpowiedź yła równa 1
#
# Po przeprowadzeniu symulacji program generuje wykresy i histogramy dla analizy wyników.
#
#
# Autor: Oskar Swat


import matplotlib.pyplot as plt
import random
import numpy as np
from scipy.stats import norm
import matplotlib.image as mpimg
from scipy.stats import triang


"""
print("Podaj wagę (kg):")
waga = float(input()) 

print("Podaj ile razy najwięcej wycisnąłeś {} kilogramów na klatę:".format(waga))
max = float(input()) 
"""

waga = 74
max = 15

powtorzenia = 0

suma_etap_1 = [0, 0, 0, 0]
suma_etap_2 = [0, 0, 0, 0]
suma_etap_3 = [0, 0, 0]
suma_etap_4 = [0, 0, 0, 0]
suma_etap_5 = [0, 0]

ilosc_los = 8000 # ilość losowań - ilość zasymulowanych treningów

wynik_powtorzenia = [powtorzenia for _ in range(ilosc_los)]

for n in range(ilosc_los):
    los = [0, 0, 0, 0, 0]
    przebieg = [0, 0, 0, 0, 0]

    for i in range(len(los)):
        los[i] = random.random()

    ############# ETAP 1 - SEN #############
    if los[0] < 0.25:
        wynik_powtorzenia[n] += round(max * 0.1)
        przebieg[0] = 1
        suma_etap_1[0] += 1
    elif los[0] <= 0.50:
        wynik_powtorzenia[n] += round(max * 0.2)
        przebieg[0]  = 2
        suma_etap_1[1] += 1
    elif los[0] <= 0.75:
        wynik_powtorzenia[n] += round(max * 0.3)
        przebieg[2]  = 3
        suma_etap_1[2] += 1
    else:
        wynik_powtorzenia[n] += round(max * 0.35)
        przebieg[0] = 4
        suma_etap_1[3] += 1


    ############# ETAP 2 - POPRZEDNI TRENING #############
    if los[1] < 0.05:
        wynik_powtorzenia[n] += round(max * 0.1)
        przebieg[1] = 1
        suma_etap_2[0] += 1
        los[4] += random.gauss(0.01, 0.005)  # Zwiększenie szansy na kontuzję barku
    elif los[1] <= 0.65:
        wynik_powtorzenia[n] += round(max * 0.2)
        przebieg[1] = 2
        suma_etap_2[1] += 1
    elif los[1] <= 0.9:
        wynik_powtorzenia[n] += round(max * 0.3)
        przebieg[1] = 3
        suma_etap_2[2] += 1
    else:
        wynik_powtorzenia[n] += round(max * 0.1)
        przebieg[1] = 4
        suma_etap_2[3] += 1


    ############# ETAP 3 - KOFEINA #############
    if los[2] < 0.1:
        wynik_powtorzenia[n] += round(max * 0)
        przebieg[2] = 1
        suma_etap_3[0] += 1
    elif los[2] <= 0.8:
        wynik_powtorzenia[n] += round(max * 0.15)
        przebieg[2] = 2
        suma_etap_3[1] += 1
    else:
        wynik_powtorzenia[n] += round(max * 0.2)
        przebieg[2] = 3
        suma_etap_3[2] += 1


    ############# ETAP 4 - ROZGRZEWKA #############
    if los[3] < 0.1:
        wynik_powtorzenia[n] += round(max * 0.1)
        przebieg[3] = 1
        los[4] += random.gauss(0.1, 0.05)  # Zwiększenie szansy na kontuzję barku
        suma_etap_4[0] += 1
    elif los[3] <= 0.55:
        wynik_powtorzenia[n] += round(max * 0.2)
        przebieg[3] = 2
        suma_etap_4[1] += 1
    elif los[3] <= 0.8:
        wynik_powtorzenia[n] += round(max * 0.3)
        przebieg[3] = 3
        suma_etap_4[2] += 1
    else:
        #print("Rozgrzewałeś się więcej niż 45 min")
        wynik_powtorzenia[n] += round(max * 0)
        przebieg[3] = 4
        los[4] += 0.01
        suma_etap_4[3] += 1


    ############# ETAP 5 - KONTUZJA BARKU #############
    if los[4] <= random.gauss(0.97, 0.01):
        wynik_powtorzenia[n] += 0
        przebieg[4] = 1
        suma_etap_5[0] += 1
    else:
        wynik_powtorzenia[n] = 0
        przebieg[4] = 2
        suma_etap_5[1] += 1

# Histogram bez 0
wynik_powtorzenia_zero = [val for val in wynik_powtorzenia if val != 0]

# Zwykły histogram
plt.figure(figsize=(16, 8))

plt.subplot(1, 2, 1)
plt.hist(wynik_powtorzenia, bins=50, edgecolor='black', alpha=0.7)
plt.title('Zwykły Histogram')
plt.xlabel('Wartości')
plt.ylabel('Częstość')

bins_powtorzenia = len(set(wynik_powtorzenia))
# Histogram z dopasowaną krzywą, pomijając 0
plt.subplot(1, 2, 2)
plt.hist(wynik_powtorzenia_zero, bins=bins_powtorzenia-1, edgecolor='black', density=True, alpha=0.7)
plt.title('Histogram z Dopasowaną Krzywą (bez treningów, gdzie ilość powtózeń wyniosła 0)')
plt.ylabel('Częstość')

# Obliczenie parametrów rozkładu normalnego
mu, std = norm.fit(wynik_powtorzenia_zero)

# Wygenerowanie danych do krzywej
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)

# Wykreślenie krzywej dopasowania
plt.plot(x, p, 'k', linewidth=2, label='Dopasowany rozkład normalny')

plt.xlabel("Wartości \n Średnia (mu): {} \n Odchylenie standardowe (std): {}".format(mu, std))
plt.legend()
plt.savefig('wykres_histogram.jpeg')
plt.show()



# Wykresy etapów
etapy = ["Etap 1 - Sen", "Etap 2 - Poprzedni Trening", "Etap 3 - Kofeina", "Etap 4 - Rozgrzewka", "Etap 5 - Kontuzja Barku"]
suma_etap = [suma_etap_1, suma_etap_2, suma_etap_3, suma_etap_4, suma_etap_5]

for i in range(5):
    ilosci = suma_etap[i]  
    etykiety = [f'Odp {j + 1}: {ilosci[j]}' for j in range(len(ilosci))] 
    plt.subplot(2, 3, i+1)
    plt.bar(range(1, len(ilosci) + 1), ilosci)
    plt.title(etapy[i])
    plt.ylabel('Ilość')

plt.tight_layout()
plt.savefig('wykres_etapy.jpeg')
plt.show()

# Zapisz wyniki symulacji do pliku
with open('wyniki_symulacji.txt', 'w') as file:
    for wynik in wynik_powtorzenia:
        file.write(str(wynik) + '\n')

with open('wyniki_symulacji_bez0.txt', 'w') as file:
    for wynik in wynik_powtorzenia_zero:
        file.write(str(wynik) + '\n')