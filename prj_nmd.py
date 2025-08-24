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
    
    @staticmethod
    def calculate_story_score(doubts_card: Card, more_card: Card, no_card: Card) -> Tuple[int, str]:
        """
        Oblicza punkty za spójność logiczną historii
        Zwraca (punkty, uzasadnienie)
        """
        all_tags = doubts_card.tags + more_card.tags + no_card.tags
        common_tags = set(doubts_card.tags) & set(more_card.tags) & set(no_card.tags)
        pair_matches = (
            len(set(doubts_card.tags) & set(more_card.tags)) +
            len(set(doubts_card.tags) & set(no_card.tags)) +
            len(set(more_card.tags) & set(no_card.tags))
        )
        
        # Obliczanie punktów
        score = 0
        justification = []
        
        # Punkty za wspólne tagi wszystkich kart
        if len(common_tags) >= 2:
            score += 5
            justification.append(f"Doskonała spójność tematyczna ({', '.join(common_tags)})")
        elif len(common_tags) == 1:
            score += 3
            justification.append(f"Dobra spójność tematyczna ({list(common_tags)[0]})")
        
        # Punkty za pary kart
        if pair_matches >= 4:
            score += 3
            justification.append("Świetne połączenia między kartami")
        elif pair_matches >= 2:
            score += 2
            justification.append("Dobre połączenia między kartami")
        elif pair_matches >= 1:
            score += 1
            justification.append("Podstawowe połączenia między kartami")
        if "mystery" in doubts_cards.tags and "supernatural" in more_cards.tags and "science" in no_cards.tags:
            score += 2
        justification.append("Bonus: Rozwiązanie naukowe zagadki supernatural")
        if "people" in all_tags and "routine" in all_tags:
           score += 1
        justification.append("Bonus: Historia o ludzkich zachowaniach")
        # Bonus za specjalne kombinacje
        
        
        # Minimalne punkty
        if score == 0:
            score = 1
            justification.append("Podstawowe punkty za próbę")
        
        return score, " | ".join(justification)





class PlayerStats:
    """System statystyk gracza"""
    
    def __init__(self):
        self.total_games = 0
        self.total_score = 0
        self.best_score = 0
        self.best_story = ""
        self.favorite_tags = {}
        self.history = []
    
    def update(self, score: int, story: str, tags: List[str]):
        """Aktualizacja statystyk po grze"""
        self.total_games += 1
        self.total_score += score
        
        if score > self.best_score:
            self.best_score = score
            self.best_story = story
        
        # Śledzenie ulubionych tagów
        for tag in tags:
            self.favorite_tags[tag] = self.favorite_tags.get(tag, 0) + 1
        
        # Historia gier
        self.history.append({
            'date': datetime.now().isoformat(),
            'score': score,
            'story': story
        })
        
        # Zachowaj tylko ostatnie 20 gier
        if len(self.history) > 20:
            self.history = self.history[-20:]

    def get_average_score(self) -> float:
        """Średni wynik"""
        if len(self.scores) == 0:  
        return 0.0
    return sum(self.scores) / len(self.scores) 
        
    
    def get_top_tags(self, limit=5) -> List[Tuple[str, int]]:
        """Najpopularniejsze tagi gracza""" 
            all_tags = []   
    for card_category in ['doubts', 'more', 'no']:
        for card in getattr(self, card_category):  
            all_tags.extend(card.tags)    
    tag_counts = {}
    for tag in all_tags:
        if tag in tag_counts:
            tag_counts[tag] += 1
        else:
            tag_counts[tag] = 1    
    sorted_tags = sorted(tag_counts.items(), key=lambda x: x[1], reverse=True)    
    return sorted_tags[:limit]
        ## Wykorzystaj sorted!       





class NoMoreDoubtsGame:
    """Główna klasa gry - korzysta z powyższych funkcji"""





if __name__ == "__main__":
    game = NoMoreDoubtsGame()

    game.run()




