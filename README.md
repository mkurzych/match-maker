# MatchMaker
## Opis
Projekt polega na stworzeniu aplikacji, która na podstawie danych demograficznych użytkowników, ich osobowości oraz zainteresowań, będzie w stanie przewidzieć, czy dana para będzie się dobrze dogadywać. Przeprowadzono analizę z użyciem drzew decyzyjnych, K-Nearest Neighbors, Gaussian Naive Bayes oraz sieci neuronowych. Serwer został napisany w języku Python z wykorzystaniem technologii Flask, natomiast klient został napisany w języku Go z użyciem biblioteki Huh.

## Architektura aplikacji

Aplikacja składa się z dwóch głównych komponentów: serwera i klienta.

- **Serwer**: Napisany w języku Python z wykorzystaniem frameworku Flask. Serwer jest odpowiedzialny za:
    - Przetwarzanie danych użytkowników.
    - Wdrażanie modeli uczenia maszynowego.
    - Obsługę zapytań od klienta i zwracanie przewidywań.
- **Klient**: Napisany w języku Go z wykorzystaniem biblioteki Huh. Klient jest odpowiedzialny za:
    - Interakcję z użytkownikiem, zbieranie danych wejściowych.
    - Przesyłanie danych do serwera i odbieranie wyników przewidywań.
    - Prezentację wyników użytkownikowi w przystępny sposób.

## Uruchomienie aplikacji
By uruchomić aplikację, należy wykonać następujące kroki:
1. Sklonować repozytorium na lokalny komputer.
2. Aktywować środowisko wirtualne:
    ```
    conda activate
    ```
3. Przejść do katalogu `server` i uruchomić serwer za pomocą komendy:
    ```
    python main.py
    ```
4. Przejść do katalogu głównego i uruchomić klienta za pomocą komendy:
    ```
   ./matchmaker.sh
    ```
5. Postępować zgodnie z instrukcjami na ekranie.

## Dane
Zestaw danych ["Speed Dating Experiment"](https://www.kaggle.com/datasets/mexwell/speed-dating) pochodzi z eksperymentu przeprowadzonego przez grupę badaczy, którzy zbierali informacje podczas sesji szybkich randek (speed dating) w latach 2002-2004. Eksperyment miał na celu zrozumienie preferencji randkowych oraz czynników wpływających na decyzje o potencjalnym dopasowaniu między uczestnikami. Dane zostały zgromadzone na Columbia University.

## Preprocessing
Dane zostały poddane obróbce w celu usunięcia zbędnych kolumn, uzupełnienia brakujących wartości oraz zakodowania kolumn kategorycznych. 
#### Usuwanie zbędnych kolumn
Usunięto kolumny „goal”, „like” i „prob”. Kolumna „goal” nie była opisana i nie miała oczywistego znaczenia (zawierała dane numeryczne bez kontekstu). Kolumna „like” zawierała ogólną ocenę osoby po randce, stanowiąc łączną ocenę wynikającą z innych kolumn („attr”, „sinc” itd.). Została usunięta, aby uprościć analizę i interakcję z danymi. Kolumna „prob” zawierała subiektywną ocenę randki i również została usunięta z tego samego powodu.

#### Uzupełnianie brakujących wartości
Brakujące wartości zostały uzupełnione medianą odpowiednich kolumn.

#### Kodowanie kolumn kategorycznych
Kolumny „career” i „met” zostały zakodowane na bardziej ogólne kategorie. Dane w kolumnie „career” zostały skategoryzowane do 14 kategorii, reprezentujących najczęściej pojawiające się branże. Kolumna „met” została uproszczona do wartości binarnych.

#### Skalowanie danych
Dane zostały zeskalowane Standard Scaler.

## Drzewo decyzyjne
#### Dokładność modelu

Testowa dokładność modelu została obliczona na podstawie pięciu powtórzeń:

```
Test accuracy = (0.70 + 0.71 + 0.70 + 0.70 + 0.71) / 5 = 0.704
```

Średnia dokładność wynosi 0.704, co oznacza, że model poprawnie klasyfikuje około 70.4% przypadków na danych testowych. Jest to umiarkowany wynik, który wskazuje na to, że model ma pewne ograniczenia w przewidywaniu, ale również jest w stanie dokonać trafnych przewidywań w większości przypadków.

#### Macierz konfuzji

Macierz konfuzji przedstawia szczegółowy podział wyników klasyfikacji:

![](/models/tree_matrix.png)
 
#### Wnioski

Model drzewa decyzyjnego osiąga umiarkowaną dokładność (70.4%) w przewidywaniu, czy para będzie się dobrze dogadywać, co oznacza, że jest stosunkowo skuteczny, ale ma również miejsce na poprawę. Analiza macierzy konfuzji sugeruje, że model ma nieco lepsze wyniki w identyfikacji braku dopasowań niż w identyfikacji dopasowań.

## K-Nearest Neighbors
#### Dokładność modelu

Najlepsza testowa dokładność modelu KNN została obliczona na podstawie pięciu powtórzeń:

```
Best KNN accuracy= (0.74 + 0.75 + 0.73 + 0.76 + 0.745) / 5 = 0.744
```

Średnia dokładność wynosi 0.744, co oznacza, że model poprawnie klasyfikuje około 74.4% przypadków na danych testowych. Jest to dobry wynik, wskazujący, że model KNN działa skutecznie w przewidywaniu dopasowania par.

#### Wybór najlepszego K

Najlepsza wartość K zazwyczaj mieści się w przedziale 15-20. Wartość K=15 została uznana za odpowiednią do dalszej analizy.

#### Macierz konfuzji dla K=15

Macierz konfuzji przedstawia szczegółowy podział wyników klasyfikacji dla K=15:

![](/models/KNN_matrix.png)

#### Wnioski

Model K-Nearest Neighbors osiąga dobrą dokładność (74.4%) w przewidywaniu, czy para będzie się dobrze dogadywać, co oznacza, że jest stosunkowo skuteczny. Analiza macierzy konfuzji i sugeruje, że model jest dobrze zrównoważony i skuteczny w identyfikowaniu zarówno dopasowań, jak i braków dopasowań.

W porównaniu do modelu drzewa decyzyjnego, model KNN ma wyższą dokładność i lepsze metryki oceny, co wskazuje na jego lepszą wydajność w tym konkretnym zadaniu.

## Gaussian Naive Bayes
#### Dokładność modelu

Testowa dokładność modelu Gaussian Naive Bayes została obliczona na podstawie pięciu powtórzeń:

```
Naive Bayes accuracy = (0.71 + 0.71 + 0.72 + 0.59 + 0.71) / 5 = 0.688 
```

Średnia dokładność wynosi 0.688, co oznacza, że model poprawnie klasyfikuje około 68.8% przypadków na danych testowych. Jest to umiarkowany wynik, który wskazuje na pewne ograniczenia modelu w przewidywaniu dopasowania par.

#### Macierz konfuzji

Macierz konfuzji przedstawia szczegółowy podział wyników klasyfikacji:

![](/models/GNB_matrix.png)

#### Wnioski

Model Gaussian Naive Bayes osiąga umiarkowaną dokładność (68.8%) w przewidywaniu, czy para będzie się dobrze dogadywać. Analiza macierzy konfuzji sugeruje, że model ma pewne ograniczenia, ale jest w stanie dostarczyć użytecznych przewidywań.

W porównaniu do modeli drzewa decyzyjnego i KNN, model Gaussian Naive Bayes ma nieco niższą dokładność i gorsze metryki oceny, co wskazuje, że może nie być tak skuteczny w tym konkretnym zadaniu. Jednakże, jego prostota i szybkość działania mogą być zaletami w niektórych kontekstach.

## Model Sieci Neuronowej

#### Dokładność modelu
Model sieci neuronowej osiągnął dokładność 76% (0.76) na danych testowych. Oznacza to, że model poprawnie klasyfikuje 76% przypadków, co wskazuje na dobrą wydajność w przewidywaniu, czy para będzie się dobrze dogadywać.

![](/models/model.py_plot.png)

#### Architektura modelu
Model został zdefiniowany jako sekwencyjna sieć neuronowa składająca się z następujących warstw:

1. **Warstwa Dense**: 128 neuronów, funkcja aktywacji 'relu', z input_shape=(input_shape,).
2. **Warstwa Dropout**: współczynnik dropout 0.5.
3. **Warstwa Dense**: 64 neurony, funkcja aktywacji 'relu'.
4. **Warstwa Dropout**: współczynnik dropout 0.5.
5. **Warstwa Dense**: 32 neurony, funkcja aktywacji 'relu'.
6. **Warstwa Dropout**: współczynnik dropout 0.5.
7. **Warstwa Dense**: 1 neuron, funkcja aktywacji 'sigmoid'.

Model jest kompilowany z optymalizatorem 'adam' i funkcją straty 'binary_crossentropy'. Metryką oceny jest dokładność ('accuracy').

#### Trening modelu
Model był trenowany z następującymi parametrami:

- **Liczba epok**: 60
- **Rozmiar batcha**: 32
- **Validation split**: 0.2 (20% danych treningowych używane jest do walidacji)
- **Callbacki**: `history`, `checkpoint`, `early_stopping`

#### Callbacki
- **history**: Zapisuje historię treningu modelu.
- **checkpoint**: Zapisuje najlepsze wagi modelu na podstawie wyników walidacji.
- **early_stopping**: Przerywa trening, jeśli wyniki walidacji nie poprawiają się przez określoną liczbę epok.

#### Macierz konfuzji

Macierz konfuzji przedstawia szczegółowy podział wyników klasyfikacji:

![](/models/model.py_matrix.png)

#### Metryki oceny
Model osiągnął dokładność 76% na danych testowych, co sugeruje, że model jest dobrze wytrenowany i generalizuje na nowych danych. Dokładność jest wyższa niż w przypadku modelu drzewa decyzyjnego (70.4%), KNN (74.4%), i GNB (68.8%).

#### Wnioski
Model sieci neuronowej wykazuje dobrą wydajność w zadaniu klasyfikacji dopasowania par, osiągając dokładność 76%. Jest to najlepszy wynik spośród wszystkich analizowanych modeli (drzewo decyzyjne, KNN, GNB). Architektura modelu z wieloma warstwami Dense i Dropout zapewnia zdolność modelu do uchwycenia złożonych wzorców w danych, jednocześnie minimalizując ryzyko przetrenowania dzięki zastosowaniu warstw Dropout.

Podsumowując, model sieci neuronowej jest skuteczny w przewidywaniu dopasowania par i może być dalej udoskonalany w celu osiągnięcia jeszcze lepszych wyników.

### Wnioski

Aplikacja do przewidywania dopasowania par wykazuje dobre wyniki, szczególnie w przypadku sieci neuronowej, która osiągnęła najwyższą dokładność (76%). Każdy z modeli ma swoje zalety i wady:

- **Drzewo decyzyjne**: Szybkie i łatwe do interpretacji, ale mniej dokładne niż KNN i sieć neuronowa.
- **KNN**: Dobrze radzi sobie z klasyfikacją, osiągając dokładność 74.4%, ale jest wolniejszy w przypadku dużych zbiorów danych.
- **Gaussian Naive Bayes**: Najszybszy model, ale najmniej dokładny, co czyni go mniej odpowiednim do tego zadania.
- **Sieć neuronowa**: Najbardziej złożony i dokładny model, który najlepiej przewiduje dopasowania par.

## Źródła 
- Fragmenty kodu z zadań laboratoryjnych
- https://scikit-learn.org/stable/modules/tree.html
- https://scikit-learn.org/stable/modules/neighbors.html
- https://scikit-learn.org/stable/modules/naive_bayes.html
- https://www.kaggle.com/datasets/mexwell/speed-dating
