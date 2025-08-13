"""
NO MORE DOUBTS - Digital CLI Version
Gra w wersji tekstowej dla pojedynczego gracza
"""

import random
import json
import os
from typing import Dict, List, Tuple
from datetime import datetime

class Card:
    def __init__(self, card_id: int, category: str, text: str, tags: List[str]):
        self.card_id = card_id
        self.category = category  # "no", "more", "doubts"
        self.text = text
        self.tags = tags  # identyfikatory tematyczne do sprawdzania logiki
    
    def __str__(self):
        return f"[{self.category.upper()}] {self.text}"


class GameDatabase:
    """Baza danych z kartami i systemem tagowania"""

    def __init__(self):
        self.cards = {
            "doubts": [],
            "more": [],
            "no": []
        }
        self._initialize_cards()
    
        self.initialize_cards()
    
    def initialize_cards(self):
        """Inicjalizacja bazy kart z tagami tematycznymi"""

        # DOUBTS - sytuacje wymagające wyjaśnienia
        doubts_data = [
            ("Dlaczego wszyscy mieszkańcy małego miasteczka noszą tylko czerwone buty?", 
             ["city", "people", "clothes", "mystery", "color"]),
            ("Co się stało z wszystkimi lewymi skarpetkami na świecie?", 
             ["clothes", "mystery", "home", "lost"]),
            ("Dlaczego koty zawsze patrzą na pusty róg pokoju?", 
             ["animals", "home", "supernatural", "mystery"]),
            ("Czemu w parku każdego dnia o 15:00 zbierają się tłumy ludzi?", 
             ["park", "people", "time", "routine", "mystery"]),
            ("Dlaczego wszystkie zegary w mieście spieszczą się o 3 minuty?", 
             ["time", "city", "technology", "mystery"]),
            ("Co oznaczają dziwne symbole pojawiające się na murach?", 
             ["city", "symbols", "mystery", "communication"]),
            ("Dlaczego ptaki unikają lądowania w centrum miasta?", 
             ["animals", "city", "nature", "mystery"]),
            ("Czemu wszyscy sąsiedzi wychodzą z domu dokładnie o tej samej porze?", 
             ["people", "routine", "mystery", "home"]),
        ]
        
        # MORE - szczegóły uzupełniające
        more_data = [
            ("Pojawia się dziwny zapach wanilii", ["smell", "mystery", "supernatural"]),
            ("Wszyscy mówią szeptem", ["people", "communication", "mystery"]),
            ("Wydarzenie powtarza się co pełnię księżyca", ["time", "routine", "supernatural"]),
            ("Słychać dźwięki kroków na poddaszu", ["home", "mystery", "supernatural"]),
            ("Temperatura zawsze spada o 5 stopni", ["weather", "mystery", "supernatural"]),
            ("Pojawiają się ślady dziwnych stóp", ["mystery", "animals", "supernatural"]),
            ("Wszystkie aparaty fotograficzne się psują", ["technology", "mystery", "supernatural"]),
            ("Dzieci zaczynają śpiewać tę samą piosenkę", ["people", "mystery", "communication"]),
            ("Elektryczność migocze w całej okolicy", ["technology", "mystery", "city"]),
            ("Pojawiają się nieznane wcześniej rośliny", ["nature", "mystery", "supernatural"]),
        ]
        
        # NO - pewne odpowiedzi/wyjaśnienia
        no_data = [
            ("To międzynarodowy spisek sprzedawców obuwia", ["conspiracy", "commercial", "people"]),
            ("Istnieje portal do krainy zaginionych rzeczy", ["supernatural", "mystery", "lost"]),
            ("Widzą duchy poprzednich mieszkańców", ["supernatural", "mystery", "home"]),
            ("To efekt lokalnego pola magnetycznego", ["science", "technology", "mystery"]),
            ("Ukryty nadajnik kontroluje ich zachowanie", ["technology", "conspiracy", "people"]),
            ("To sekretny eksperyment rządowy", ["conspiracy", "government", "science"]),
            ("Miejscowy artysta tworzy instalację miejską", ["art", "city", "people"]),
            ("To tradycja przekazywana z pokolenia na pokolenie", ["culture", "people", "routine"]),
            ("Badacze testują nową teorię naukową", ["science", "people", "mystery"]),
            ("To skutek działania nowego leku na alergię", ["medicine", "science", "people"]),
        ]

        # Tworzenie obiektów Card
        for i (text, tags) in enumerate(doubts_data):
            self.cards["doubts"].append(Card.i, "doubts", text, tags)
        for i, (text, tags) in enumerate(more_data):
            self.cards["more"].append(Card.i, "more", text, tags)
        for i, (text, tags) in enumerate(no_data):
           self.cards["no"].append(Card.i, "no", text, tags)
        # uzupełnij dla reszty kategorii




class LogicAnalyzer:
    """System analizy logiki historii oparty na tagach"""





class PlayerStats:
    """System statystyk gracza"""





class NoMoreDoubtsGame:
    """Główna klasa gry - korzysta z powyższych funkcji"""





if __name__ == "__main__":
    game = NoMoreDoubtsGame()

    game.run()
