## **1. Na czym polega gra**

* Gra nazywa się **NO MORE DOUBTS – Digital CLI Version** i działa w terminalu (CLI).
* Masz **trzy kategorie kart**:

  1. **DOUBTS** – zagadkowa sytuacja (pytanie lub problem).
  2. **MORE** – dodatkowe szczegóły uzupełniające.
  3. **NO** – wyjaśnienie lub rozwiązanie.
* W każdej nowej rozgrywce:

  1. Dostajesz **po 3 losowe karty** z każdej kategorii.
  2. Wybierasz po **jednej** z każdej kategorii.
  3. Tworzysz historię w kolejności **DOUBTS → MORE → NO**.
  4. Program ocenia spójność historii na podstawie **tagów tematycznych** przypisanych do kart.
* Wynik to liczba punktów z uzasadnieniem (0–10+), a program zapisuje twoje statystyki.

---

## **2. Jak działa ocena historii**

* Każda karta ma listę **tagów** (np. `"mystery"`, `"people"`, `"technology"`) opisujących jej temat.
* System sprawdza:

  * **Wspólne tagi we wszystkich trzech kartach** (dają dużo punktów).
  * **Dopasowania między parami kart** (mniej punktów, ale nadal ważne).
  * **Specjalne kombinacje** (np. zagadka → nadprzyrodzone szczegóły → naukowe wyjaśnienie daje bonus).
  * Minimalnie zawsze dostajesz **1 punkt za próbę**.
* Wynik + uzasadnienie wyświetlane są od razu po grze.

---

## **3. Jak działa zapis postępu**

* Program zapisuje dane w pliku `nmd_stats.json`:

  * liczba gier,
  * suma punktów i średnia,
  * najlepszy wynik i najlepsza historia,
  * najczęściej używane tagi,
  * historia ostatnich 20 gier.
* Możesz w menu zobaczyć:

  * **statystyki** (opcje 2),
  * **historię gier** (opcja 3),
  * **zasady** (opcja 4).

---

## **4. Struktura kodu**

Kod jest podzielony na klasy:

| Klasa                  | Zadanie                                                                              |
| ---------------------- | ------------------------------------------------------------------------------------ |
| **`Card`**             | Reprezentuje pojedynczą kartę (ID, kategoria, tekst, tagi).                          |
| **`GameDatabase`**     | Przechowuje wszystkie karty w 3 kategoriach, inicjalizuje je z opisami i tagami.     |
| **`LogicAnalyzer`**    | Analizuje historię na podstawie kart, przyznaje punkty i pisze uzasadnienie.         |
| **`PlayerStats`**      | Przechowuje i aktualizuje statystyki gracza oraz jego ulubione tagi.                 |
| **`NoMoreDoubtsGame`** | Główna logika gry: menu, rozgrywka, zapis/wczytanie statystyk, wyświetlanie wyników. |

---

## **5. Przepływ działania programu**

1. **Start programu** → `game.run()` uruchamia główną pętlę menu.
2. **Menu** → wybierasz jedną z opcji (nowa gra, statystyki, historia, zasady, wyjście).
3. **Nowa gra**:

   * Losowanie po 3 karty z każdej kategorii (`random.sample`).
   * Wyświetlenie i wybór jednej z każdej kategorii.
   * Tworzenie historii i analiza przez `LogicAnalyzer`.
   * Aktualizacja statystyk i zapis do pliku JSON.
4. **Po grze** → motywacyjna wiadomość zależna od wyniku.
5. **Powrót do menu** lub zakończenie programu.

---

## **6. Technologie i techniki użyte w kodzie**

* **Python 3** + standardowe biblioteki (`random`, `json`, `os`, `datetime`).
* **Obiektowe podejście** – każda część gry ma swoją klasę.
* **System tagów** – prosty sposób oceny spójności historii.
* **Zapisywanie stanu gry** – plik JSON jako baza statystyk.
* **Interfejs tekstowy** – obsługa przez wiersz poleceń (CLI).
