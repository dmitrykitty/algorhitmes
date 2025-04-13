"""
Indeks h (indeks Hirscha) to wskaźnik bibliometryczny oceniający dorobek naukowców. Uwzględnia liczbę publikacji
i ich cytowań. Naukowiec ma indeks h, jeśli h spośród jego publikacji ma ≥h cytowań każda, a pozostałe ≤h cytowań.

Zaimplementuj funkcję hIndex(citations: List[int]), która dla tablicy cytowań publikacji zwróci indeks h.
Założenia:
1. Tablica zawiera wszystkie prace autora
2. Liczba prac: 1 ≤ N ≤ 1000
3. Cytowania per praca: 0 ≤ c ≤ 1000
4. Złożoność czasowa: O(n)

Przykład 1:
Wejście: [3, 0, 6, 1, 5] → 3 publikacje z ≥3 cytowaniami (6,5,3) i 2 z ≤3 cytowań (1,0)

Przykład 2:
Wejście: [1, 3, 1] → 1 publikacja z ≥1 cytowaniem (3) i 2 z ≤1 cytowań (1,1)

Przykład 3:
Wejście: [1, 2, 3, 1, 1] → 2 publikacje z ≥2 cytowaniami (3,2) i 3 z ≤2 cytowań (1,1,1)
"""


def hIndex(citations):
    max_val = citations[0]
    sum_c = 0
    for i in range(1, len(citations)):
        max_val = max(max_val, citations[i])

    count = [0] * (max_val + 1)

    for i in range(len(citations)):
        count[citations[i]] += 1

    for i in range(max_val, -1, -1):
        sum_c += count[i]
        if sum_c >= i:
            return i

    return 0


citation = [1, 2, 3, 1, 1, ]
print(hIndex(citation))
